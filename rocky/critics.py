"""Rule-based critics: the ambiguities a program can find without a model.

Each critic returns attention items::

    {"kind": ..., "severity": 1-5, "class_id": ..., "code": ..., "name": ...,
     "explanation": ..., "options": [...], "affects": [...], "framing_ref": ...}

``rank`` orders items by severity × blast radius (1 + number of classes and
systems the item touches). The critique skill adds what these rules miss.
"""

from __future__ import annotations

import re
from collections import defaultdict

from .table import Table

CATCH_ALL = re.compile(r"\b(other|others|mosaic|miscellaneous|unclassified|not observed|no data|undifferentiated|mixed|various)\b", re.I)
LAND_USE = {
    "pasture": "LU_PrimaryProductionActivities (livestock grazing)", "grazing": "LU_PrimaryProductionActivities (livestock grazing)",
    "rangeland": "LU_PrimaryProductionActivities (livestock grazing)", "mining": "LU_RawEndProductionIndustryActivities (extraction)",
    "quarry": "LU_RawEndProductionIndustryActivities (extraction)", "aquaculture": "LU_PrimaryProductionActivities (aquaculture)",
    "silviculture": "LU_PrimaryProductionActivities (forestry)", "forest plantation": "LU_PrimaryProductionActivities (forestry)",
    "planted forest": "LU_PrimaryProductionActivities (forestry)", "plantation": "LU_PrimaryProductionActivities (perennial crops)",
    "agriculture": "LU_PrimaryProductionActivities (crop cultivation)", "cropland": "LU_PrimaryProductionActivities (crop cultivation)",
    "crop": "LU_PrimaryProductionActivities (crop cultivation)", "farming": "LU_PrimaryProductionActivities",
    "urban": "LU_ResidentialActivities", "infrastructure": "LU_TransportActivities / LU_UtilitiesActivities",
    "industrial": "LU_HeavyProductionIndustryActivities", "park": "LU_ProvisionActivities (recreation)",
    "sport": "LU_ProvisionActivities (recreation)", "protected": "LU_ConservationProtectionActivities",
    "reserve": "LU_ConservationProtectionActivities", "photovoltaic": "LU_EnergyProductionIndustryActivities",
    "solar": "LU_EnergyProductionIndustryActivities", "fallow": "LU_PrimaryProductionActivities (fallow)",
}


_NAME_STOP = {"formation", "formations", "area", "areas", "natural", "vegetation", "of", "and", "or", "the", "a",
              "other", "non", "type", "types", "pan", "mapbiomas", "standard", "code", "not", "in", "legend", "beta",
              "used", "by", "rasters", "place", "color", "from", "palette", "s", "lands", "land", "body", "bodies"}
# spelling and near-synonym normalisation for class names; deliberately small and physical
_NAME_SYNONYMS = {
    "scrub": "shrub", "scrubland": "shrub", "scrublands": "shrub", "shrubland": "shrub", "shrublands": "shrub", "shrubs": "shrub", "shrubby": "shrub",
    "woodland": "forest", "woodlands": "forest", "forests": "forest", "wooded": "forest",
    "floodable": "flooded", "flood": "flooded", "inundated": "flooded",
    "glacier": "ice", "glaciers": "ice", "snow": "ice",
    "infrastructure": "urban", "built": "urban", "settlement": "urban",
    "silviculture": "plantation", "planted": "plantation", "plantations": "plantation",
    "agricultural": "agriculture", "farming": "agriculture", "cropland": "agriculture", "crops": "agriculture", "crop": "agriculture",
    "pastures": "pasture", "grasslands": "grassland", "waters": "water", "bodies": "body",
}


def _name_tokens(name: str) -> frozenset:
    toks = re.findall(r"[a-z]+", name.lower())
    out = set()
    for t in toks:
        t = _NAME_SYNONYMS.get(t, t)
        if t in _NAME_STOP:
            continue
        if len(t) > 4 and t.endswith("s"):
            t = t[:-1]
        out.add(_NAME_SYNONYMS.get(t, t))
    return frozenset(out)


def _jaccard(a: frozenset, b: frozenset) -> float:
    if not a and not b:
        return 1.0
    return len(a & b) / len(a | b) if (a | b) else 1.0


def _elements(t: Table, cid: str) -> dict[tuple, dict]:
    """(hp, stratum, block) -> {ref, presence, cover:(min,max) or None}"""
    out = {}
    for hid in t.hps(cid):
        for sid in t.strata(cid, hid):
            for bid, ref in t.blocks(cid, hid, sid):
                a = t.attrs(class_id=cid, hp_id=hid, stratum_id=sid, block_id=bid, record="element")
                cov = a.get("cover")
                out[(hid, sid, bid)] = {"ref": ref, "presence": a.get("elementPresenceType").value if a.get("elementPresenceType") else "",
                                        "cover": (float(cov.min), float(cov.max)) if cov and cov.min and cov.max and _num(cov.min) and _num(cov.max) else None}
    return out


def _num(s):
    try:
        float(s)
        return True
    except (TypeError, ValueError):
        return False


def _signature(els: dict) -> frozenset:
    return frozenset(e["ref"] for e in els.values())


def _overlap(a, b) -> bool:
    if a is None or b is None:
        return True
    return not (a[1] < b[0] or b[1] < a[0])


def run_system(t: Table, classes: list[dict], framing_by_class: dict[str, list[str]] | None = None) -> list[dict]:
    """classes: [{class_id, code, name, definition, parent_code, status}]"""
    items: list[dict] = []
    framing_by_class = framing_by_class or {}
    by_id = {c["class_id"]: c for c in classes}
    els = {c["class_id"]: _elements(t, c["class_id"]) for c in classes}

    for c in classes:
        cid, code, name = c["class_id"], c.get("code", ""), c.get("name", "")
        defn = (c.get("definition") or "").strip()
        e = els[cid]
        # underspecified
        if not e:
            items.append(dict(kind="underspecified", severity=3, class_id=cid, code=code, name=name,
                              explanation="No element decomposition yet (titles only or not proposed)." if not defn
                              else "No element decomposition yet although a definition exists.",
                              options=["propose a decomposition from the name and nearest registry examples",
                                       "ask the publisher for the class definition"], affects=[]))
        else:
            missing = [k for k, v in e.items() if v["cover"] is None and v["ref"] and not v["ref"].startswith("LC_Element")]
            sibling_has = any(v["cover"] is not None for oc in classes if oc["class_id"] != cid for v in els[oc["class_id"]].values())
            if missing and sibling_has:
                items.append(dict(kind="underspecified", severity=2, class_id=cid, code=code, name=name,
                                  explanation=f"{len(missing)} element(s) have no cover range while sibling classes state one.",
                                  options=["transcribe the threshold from the source", "leave empty and mark the class as qualitative"], affects=[]))
        # catch-all
        if CATCH_ALL.search(name):
            items.append(dict(kind="catch_all", severity=2, class_id=cid, code=code, name=name,
                              explanation="The class name is a residual or mixed category; its physical content depends on what the other classes exclude.",
                              options=["define it by exclusion explicitly (list the elements it may contain)", "split it", "keep as a mapping-unit mixed class"], affects=[]))
        # land use masquerade
        low = (name + " " + defn[:200]).lower()
        for k, act in LAND_USE.items():
            if re.search(rf"\b{re.escape(k)}\b", low):
                items.append(dict(kind="land_use_masquerade", severity=3, class_id=cid, code=code, name=name,
                                  explanation=f"'{name}' names an activity ({act}), not a physical cover.",
                                  options=["describe the physical cover and record the activity as land_use_hint",
                                           "declare the system a land-use legend for this class"], affects=[], land_use_hint=act))
                break
        # mixed class without proportion
        if re.search(r"\b(mosaic|mixed|and/or|/)\b", name, re.I) and e and all(v["cover"] is None for v in e.values()):
            items.append(dict(kind="mixed_class_without_proportion", severity=3, class_id=cid, code=code, name=name,
                              explanation="A mosaic or mixed class with no proportions: comparison with other systems is impossible.",
                              options=["state the dominant component and its share", "model it as an AND mixed class with percentages"], affects=[]))

    # sibling overlap: identical element sets with overlapping covers
    sigs = defaultdict(list)
    for cid, e in els.items():
        if e:
            sigs[_signature(e)].append(cid)
    for sig, group in sigs.items():
        if len(group) < 2:
            continue
        for i, a in enumerate(group):
            for b in group[i + 1:]:
                ea, eb = els[a], els[b]
                ranges_a = {v["ref"]: v["cover"] for v in ea.values()}
                ranges_b = {v["ref"]: v["cover"] for v in eb.values()}
                if all(_overlap(ranges_a.get(r), ranges_b.get(r)) for r in sig):
                    fa, fb = framing_by_class.get(a, []), framing_by_class.get(b, [])
                    kind = "framing_only_split" if (fa or fb) and fa != fb else "sibling_overlap"
                    items.append(dict(kind=kind, severity=4, class_id=a, code=by_id[a].get("code", ""), name=by_id[a].get("name", ""),
                                      explanation=f"Same elements as {by_id[b].get('code','')} '{by_id[b].get('name','')}' with overlapping covers"
                                                  + ("; the split is explained only by framing." if kind == "framing_only_split" else "; nothing in the rows tells them apart."),
                                      options=["state the discriminating attribute (cover, height, phenology, artificiality)",
                                               "merge the two classes", "keep both and record the instrument that requires the split"],
                                      affects=[b], framing_ref=(fa or fb or [None])[0]))

    # hierarchy conflict: child's dominant element family disagrees with parent's
    fam = lambda refs: {("veg" if any(x in r for x in ("Tree", "Shrub", "Herb", "Graminoid", "Forb", "Vegetation", "GrowthForm", "Lichen", "Moss", "Algae")) else
                          "water" if any(x in r for x in ("Water", "Snow", "Ice")) else
                          "artificial" if any(x in r for x in ("Artificial", "BuiltUp", "Building", "Linear", "Extraction", "DumpSite")) else
                          "natural_surface" if any(x in r for x in ("Rock", "Soil", "Sand", "Dune", "Deposit", "Hardpan")) else "other")
                         for r in refs}
    for c in classes:
        pc = c.get("parent_code")
        if not pc or pc not in by_id:
            continue
        child, parent = els[c["class_id"]], els[pc]
        if child and parent and not (fam(_signature(child)) & fam(_signature(parent))):
            items.append(dict(kind="hierarchy_conflict", severity=4, class_id=c["class_id"], code=c.get("code", ""), name=c.get("name", ""),
                              explanation=f"Filed under {pc} '{by_id[pc].get('name','')}' but its elements belong to a different family than the parent's.",
                              options=["move the class under the parent its elements imply", "keep the hierarchy and record the instrument that requires it"],
                              affects=[pc]))
    return items


def run_cross_system(systems: dict[str, tuple[Table, list[dict]]]) -> list[dict]:
    """systems: slug -> (table, classes). Finds code collisions and threshold drift across systems."""
    items = []
    by_code: dict[str, list[tuple[str, dict, frozenset]]] = defaultdict(list)
    by_name: dict[str, list[tuple[str, dict, dict]]] = defaultdict(list)
    for slug, (t, classes) in systems.items():
        for c in classes:
            e = _elements(t, c["class_id"])
            if c.get("code"):
                by_code[c["code"]].append((slug, c, _signature(e)))
            by_name[re.sub(r"\W+", " ", c.get("name", "").lower()).strip()].append((slug, c, e))
    for code, lst in by_code.items():
        if len(lst) < 2:
            continue
        sigs = {s for _, _, s in lst if s}
        toks = [_name_tokens(c.get("name", "")) for _, c, _ in lst]
        common = frozenset.intersection(*toks) if toks else frozenset()
        identical = len(set(toks)) == 1
        if len(sigs) > 1:
            sev, why = 5, "the element decompositions differ"
        elif not common and len(sigs) <= 1:
            sev, why = 4, "the class names share no content word and no decomposition settles whether they mean the same cover"
        elif not identical and len(sigs) <= 1:
            extras = sorted(set().union(*toks) - common)
            sev, why = 2, f"the names share '{', '.join(sorted(common))}' but differ in qualifiers ({', '.join(extras[:6])}); check whether the qualifiers change the cover"
        elif len({re.sub(r'\s+', ' ', c.get('name', '').strip().lower()) for _, c, _ in lst}) > 1 and len(sigs) <= 1:
            sev, why = 1, "the names differ only in wording; probably a translation, confirm by decomposing"
        else:
            continue
        shown = sorted({c.get("name", "") for _, c, _ in lst})
        items.append(dict(kind="cross_system_collision", severity=sev, class_id=lst[0][1]["class_id"], code=code, name=lst[0][1].get("name", ""),
                          explanation=f"Code {code} is used by {len(lst)} systems as: {', '.join(shown[:8])}; {why}.",
                          options=["never compare raw codes across these systems", "decompose each and compare elements",
                                   "define a shared code table", "rename the outlier"],
                          affects=[f"{s}:{c['class_id']}" for s, c, _ in lst[1:]]))
    for name, lst in by_name.items():
        if len(lst) < 2:
            continue
        covers = {}
        for slug, c, e in lst:
            for v in e.values():
                if v["cover"] is not None:
                    covers.setdefault(v["ref"], {})[slug] = v["cover"]
        for ref, per in covers.items():
            if len(per) > 1 and len({tuple(x) for x in per.values()}) > 1:
                items.append(dict(kind="threshold_drift", severity=4, class_id=lst[0][1]["class_id"], code=lst[0][1].get("code", ""), name=lst[0][1].get("name", ""),
                                  explanation=f"'{name}' sets {ref} cover at {', '.join(f'{s}: {a:g}–{b:g} %' for s, (a, b) in per.items())}.",
                                  options=["adopt one threshold", "keep both and document the mapping as lossy"],
                                  affects=[f"{s}:{c['class_id']}" for s, c, _ in lst[1:]]))
    return items


MAX_BLAST = 5   # beyond five dependants the count says "everywhere", not "more urgent"


def rank(items: list[dict]) -> list[dict]:
    def key(i):
        blast = 1 + min(len(i.get("affects") or []), MAX_BLAST)
        return (-(i.get("severity", 1) * blast), i.get("kind", ""), i.get("code", ""))
    seen = set()
    out = []
    for i in sorted(items, key=key):
        k = (i["kind"], i["class_id"], tuple(i.get("affects") or []))
        if k in seen:
            continue
        seen.add(k)
        i["rank_score"] = i.get("severity", 1) * (1 + min(len(i.get("affects") or []), MAX_BLAST))
        out.append(i)
    return out
