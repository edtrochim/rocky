"""Score a proposed decomposition against a reference (the registry's own rows).

Per class:
  element_recall     share of reference element types the proposal contains
  element_precision  share of proposed element types the reference contains
  presence_agreement share of matched elements whose presence class agrees (fixed vs conditional)
  range_overlap      mean overlap fraction of cover ranges on matched elements where both sides state one
  stratum_count_ok   proposal has the same number of strata as the reference

Element types are compared at family granularity too (LC_Tree ~ LC_WoodyGrowthForm counts as a
partial hit), reported separately as ``family_recall``.
"""

from __future__ import annotations

from .table import Table

FAMILY = {
    "LC_Tree": "woody", "LC_Shrub": "woody", "LC_WoodyGrowthForm": "woody",
    "LC_HerbaceousGrowthForm": "herb", "LC_Graminoid": "herb", "LC_Forbs": "herb", "LC_GrowthForm": "veg", "LC_VegetationElement": "veg",
    "LC_LichenAndMoss": "cryptogam", "LC_Lichen": "cryptogam", "LC_Moss": "cryptogam", "LC_Algae": "cryptogam",
    "LC_ArtificialSurfaceElement": "artificial", "LC_BuiltUpSurface": "artificial", "LC_Building": "artificial",
    "LC_LinearSurface": "artificial", "LC_NonLinearSurface": "artificial", "LC_OtherConstruction": "artificial",
    "LC_OtherArtificialSurface": "artificial", "LC_NonBuiltUpSurface": "artificial", "LC_DumpSite": "artificial", "LC_Extraction": "artificial",
    "LC_NaturalSurfaceElement": "bare", "LC_RocksSurfaceElement": "bare", "LC_BareRock": "bare", "LC_Hardpan": "bare",
    "LC_SoilSandDepositsSurfaceElement": "bare", "LC_BareSoil": "bare", "LC_CoarseMineralFragments": "bare",
    "LC_LooseAndShiftingSand": "bare", "LC_Dune": "bare", "LC_Deposits": "bare", "LC_InorganicDeposits": "bare", "LC_OrganicDeposits": "bare",
    "LC_WaterBodyAndAssociatedSurfaceElement": "water", "LC_WaterBody": "water", "LC_Snow": "water", "LC_Ice": "water",
    "LC_TerrestrialIce": "water", "LC_FloatingIce": "water",
}
FIXED = {"fixed", "mandatory"}


def _elements(t: Table, cid: str) -> list[dict]:
    out = []
    for hid in t.hps(cid):
        for sid in t.strata(cid, hid):
            for bid, ref in t.blocks(cid, hid, sid):
                a = t.attrs(class_id=cid, hp_id=hid, stratum_id=sid, block_id=bid, record="element")
                pres = a.get("elementPresenceType") or a.get("presence_type")
                cov = a.get("cover")
                rng = None
                if cov and cov.min and cov.max:
                    try:
                        rng = (float(cov.min), float(cov.max))
                    except ValueError:
                        pass
                out.append({"stratum": sid, "ref": ref, "presence": (pres.value.lower() if pres else ""), "cover": rng})
    return out


def _overlap(a, b) -> float:
    lo, hi = max(a[0], b[0]), min(a[1], b[1])
    if hi < lo:
        return 0.0
    union = max(a[1], b[1]) - min(a[0], b[0]) or 1.0
    return (hi - lo) / union


def score_class(ref_t: Table, ref_cid: str, prop_t: Table, prop_cid: str) -> dict:
    R, P = _elements(ref_t, ref_cid), _elements(prop_t, prop_cid)
    rrefs = {e["ref"] for e in R}
    prefs = {e["ref"] for e in P}
    if not rrefs:
        return {"skipped": "reference has no elements"}
    inter = rrefs & prefs
    rfam = {FAMILY.get(r, r) for r in rrefs}
    pfam = {FAMILY.get(r, r) for r in prefs}
    # match same-type elements one-to-one in stratum order, so two tree layers do not cross-match
    matched = []
    used: set[int] = set()
    for r in R:
        for j, p in enumerate(P):
            if j not in used and r["ref"] == p["ref"]:
                matched.append((r, p))
                used.add(j)
                break
    pres_ok = [((r["presence"] in FIXED) == (p["presence"] in FIXED)) for r, p in matched if r["presence"] and p["presence"]]
    ovl = [_overlap(r["cover"], p["cover"]) for r, p in matched if r["cover"] and p["cover"]]
    return {
        "element_recall": len(inter) / len(rrefs),
        "element_precision": (len(inter) / len(prefs)) if prefs else 0.0,
        "family_recall": len(rfam & pfam) / len(rfam) if rfam else 0.0,
        "presence_agreement": (sum(pres_ok) / len(pres_ok)) if pres_ok else None,
        "range_overlap": (sum(ovl) / len(ovl)) if ovl else None,
        "stratum_count_ok": len({e["stratum"] for e in R}) == len({e["stratum"] for e in P}),
        "reference_elements": sorted(rrefs), "proposed_elements": sorted(prefs),
    }


def aggregate(scores: list[dict]) -> dict:
    valid = [s for s in scores if "skipped" not in s]
    if not valid:
        return {"classes": 0}
    def mean(key):
        vals = [s[key] for s in valid if s.get(key) is not None]
        return round(sum(vals) / len(vals), 3) if vals else None
    return {"classes": len(valid), "element_recall": mean("element_recall"), "element_precision": mean("element_precision"),
            "family_recall": mean("family_recall"), "presence_agreement": mean("presence_agreement"),
            "range_overlap": mean("range_overlap"),
            "stratum_count_ok": round(sum(1 for s in valid if s["stratum_count_ok"]) / len(valid), 3)}
