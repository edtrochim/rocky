"""Structural validation of a table against the LChS vocabulary.

This is the strict check the FAO schema cannot give (see ``schemas.py``).
It answers: is every element a known type, does every property belong to
that type, is every enum value legal, is every range sane, does every class
have at least one horizontal pattern, stratum and element.

Findings are dicts with ``level`` (error | warning), ``class_id``, ``where``
and ``message`` so a tool can print them or an agent can act on them.
"""

from __future__ import annotations

from .table import Table
from . import lchs_vocab

# Fields FAO's own files put on records although the schema does not declare them.
TOLERATED = {"name", "description", "instanceIndex", "order", "onTopID", "on_top",
             "sealed", "heightCM", "macropatternCoverage", "macropatternType", "elementID",
             "formElementID", "objectID", "objectReference"}
PERCENT_PROPS = {"cover", "portioning", "occurrence", "evergreenPercentage", "deciduousPercentage",
                 "broadLeafPercentage", "needleLeafPercentage", "aphyllousPercentage",
                 "perennialPercentage", "nonPerennialPercentage", "irrigationPercentage",
                 "rainfedPercentage", "postfloodingPercentage", "overlapGrowingPeriodPercentage"}
# LCCS3 characteristics with no LChS counterpart: legal in the older format, reported as warnings.
LCCS3_ONLY = {"LC_UserDefinedElementCharacteristic", "LC_UserDefinedCharacteristic", "LC_UserDefinedClassCharacteristic",
              "LC_NaturalSurfaceCharacteristic", "LC_ConsolidatedSurfaceCharacteristics",
              "LC_UnconsolidatedSurfaceCharacteristics", "LC_PeriodicVariations", "LC_PeriodicVariation",
              "LC_ArtificialSurfaceCharacteristic"}
# Values FAO writes in files vs the enum spelling in the typed definitions.
PRESENCE_SYNONYMS = {"fixed": "fixed", "mandatory": "fixed", "optional": "conditionalTemporal",
                     "exclusive": "exclusive", "conditional temporal": "conditionalTemporal",
                     "conditionaltemporal": "conditionalTemporal", "precluded": "precluded",
                     "temporal sequence depending": "conditionalTemporal"}


def _num(s: str):
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def validate(t: Table, vocab: lchs_vocab.LchsVocab | None = None) -> list[dict]:
    from .lchs import _normalise
    t = _normalise(t)   # LCCS3-native rows are checked in LChS terms
    v = vocab or lchs_vocab.load()
    elements = v.elements()
    chars = v.characteristics()
    out: list[dict] = []

    def add(level, class_id, where, msg):
        out.append({"level": level, "class_id": class_id, "where": where, "message": msg})

    # per-class structure
    for cid, code, name in t.classes():
        hps = t.hps(cid)
        if not hps:
            add("error", cid, "class", f"class {code or cid} '{name}' has no horizontal pattern (titles-only)")
            continue
        for hid in hps:
            strata = t.strata(cid, hid)
            if not strata:
                add("error", cid, f"hp {hid}", "horizontal pattern has no stratum")
            for sid in strata:
                if not t.blocks(cid, hid, sid):
                    add("error", cid, f"stratum {sid}", "stratum has no element")

    # element rows
    seen_blocks = set()
    for r in t.rows:
        if r.record == "element":
            key = (r.class_id, r.hp_id, r.stratum_id, r.block_id)
            if r.ref not in elements:
                if key not in seen_blocks:
                    add("error", r.class_id, f"stratum {r.stratum_id} block {r.block_id}",
                        f"unknown element type '{r.ref}'")
                seen_blocks.add(key)
                continue
            seen_blocks.add(key)
            props = {p.name: p for p in elements[r.ref].props}
            if r.attribute in TOLERATED or r.attribute == "":
                continue
            p = props.get(r.attribute)
            if p is None:
                add("error", r.class_id, f"{r.ref} in stratum {r.stratum_id}",
                    f"property '{r.attribute}' is not allowed on {r.ref}")
                continue
            _check_value(add, v, p, r, r.ref)
        elif r.record == "characteristic":
            if r.attribute in ("", "BlockReference"):
                continue
            if r.ref not in chars:
                key = (r.class_id, r.stratum_id, r.block_id, r.char_id)
                if key not in seen_blocks:
                    seen_blocks.add(key)
                    if r.ref in LCCS3_ONLY:
                        add("warning", r.class_id, f"stratum {r.stratum_id} char {r.char_id}",
                            f"characteristic '{r.ref}' exists in LCCS3 only; no LChS equivalent")
                    else:
                        add("error", r.class_id, f"stratum {r.stratum_id} char {r.char_id}",
                            f"unknown characteristic '{r.ref}'")
                continue
            props = {p.name: p for p in chars[r.ref].props}
            if r.attribute in TOLERATED or r.attribute in ("CharacteristicLabel",):
                continue
            p = props.get(r.attribute)
            if p is None:
                add("error", r.class_id, f"{r.ref} in stratum {r.stratum_id}",
                    f"field '{r.attribute}' is not allowed on {r.ref}")
                continue
            _check_value(add, v, p, r, r.ref)
        elif r.record == "stratum" and r.attribute == "presenceType" and r.value:
            if r.value.lower() not in PRESENCE_SYNONYMS:
                add("error", r.class_id, f"stratum {r.stratum_id}", f"presenceType '{r.value}' not recognised")
        elif r.record in ("hp", "stratum") and r.attribute in PERCENT_PROPS:
            _check_range(add, r, r.attribute, 0, 100)

    # covers in a stratum should not exceed 100 in their minimum (a soft check)
    for cid, code, name in t.classes():
        for hid in t.hps(cid):
            for sid in t.strata(cid, hid):
                mins = 0.0
                for bid, ref in t.blocks(cid, hid, sid):
                    a = t.attrs(class_id=cid, hp_id=hid, stratum_id=sid, block_id=bid, record="element")
                    c = a.get("cover")
                    if c is not None and _num(c.min) is not None:
                        mins += _num(c.min)
                if mins > 100:
                    add("warning", cid, f"stratum {sid}", f"minimum covers sum to {mins:g} % (> 100)")
    return out


def _check_value(add, v, p, r, owner):
    if p.is_enum:
        allowed = v.enum_values(p.type)
        val = r.value
        if val == "":
            return
        if p.name == "elementPresenceType":
            if val.lower() not in PRESENCE_SYNONYMS:
                add("error", r.class_id, owner, f"elementPresenceType '{val}' not recognised")
            return
        if v.enum_match(p.type, val) is None:
            add("error", r.class_id, owner, f"{p.name} '{val}' is not one of {allowed}")
        return
    if p.is_range:
        lo, hi = (0, 100) if p.name in PERCENT_PROPS else (None, None)
        _check_range(add, r, p.name, lo, hi, owner=owner)
    elif r.min or r.max:
        add("warning", r.class_id, owner, f"{p.name} given as a range but the schema allows a single value")


def _check_range(add, r, name, lo, hi, owner=None):
    owner = owner or r.record
    if r.min == "" and r.max == "":
        return
    a, b = _num(r.min), _num(r.max)
    if a is None or b is None:
        if r.value == "" or _num(r.value) is None:
            add("error", r.class_id, owner, f"{name} range '{r.min}..{r.max}' is not numeric")
        return
    if a > b:
        add("error", r.class_id, owner, f"{name} range {a:g}..{b:g} has min > max")
    if lo is not None and (a < lo or b > hi):
        add("error", r.class_id, owner, f"{name} range {a:g}..{b:g} outside {lo}..{hi}")


def summary(findings: list[dict]) -> dict:
    return {"errors": sum(1 for f in findings if f["level"] == "error"),
            "warnings": sum(1 for f in findings if f["level"] == "warning")}
