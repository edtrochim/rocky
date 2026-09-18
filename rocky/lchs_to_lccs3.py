"""Property-level mapping from LChS rows to LCCS3 rows, used when a table that
came from LChS (or was authored in LChS terms) is written as ``.lccs``.

LChS keeps properties flat on the element record; LCCS3 nests them in typed
containers. Only the properties both formats share are mapped; anything else
is dropped here and reported by the caller through ``dropped``. Full-range
percentages (0..100) are LChS's "unspecified" and are not written.
"""

from __future__ import annotations

from .table import Row
from . import crosswalk

WOODY_PHEN = {"evergreenPercentage": "LC_Evergreen", "deciduousPercentage": "LC_Deciduous"}
WOODY_LEAF = {"broadLeafPercentage": "LC_Broadleaved", "needleLeafPercentage": "LC_Needleleaved",
              "aphyllousPercentage": "LC_Aphillous"}
HERB_PHEN = {"perennialPercentage": "LC_Perennial", "nonPerennialPercentage": "LC_Annual"}
TEMPORAL = {"sequential same year": "Sequential Same Year", "sequentialsameyear": "Sequential Same Year",
            "sequential other year": "Sequential Other Year", "sequentialotheryear": "Sequential Other Year"}


def _copy(r: Row, **kw) -> Row:
    return Row(**{**r.__dict__, **kw})


def _cm_to_m(s: str) -> str:
    try:
        return f"{float(s) / 100:g}"
    except ValueError:
        return s


def _unspecified(r: Row) -> bool:
    return (r.min, r.max) in (("0", "100"), ("0.0", "100.0")) or (r.min == "" and r.max == "" and r.value == "")


def hp_rows(rows: list[Row]) -> list[Row]:
    out = []
    for r in rows:
        if r.attribute == "occurrence":
            out.append(_copy(r, attribute="occurance"))
        elif r.attribute in ("name", "description", "type", "cover", "occurance"):
            out.append(r)
    return out


def stratum_rows(rows: list[Row]) -> list[Row]:
    out = []
    for r in rows:
        if r.attribute == "presenceType":
            out.append(_copy(r, attribute="presence_type",
                             value=crosswalk.PRESENCE_LCHS_TO_LCCS3.get(r.value, "Mandatory")))
        elif r.attribute == "onTop":
            out.append(_copy(r, attribute="@ontop", value=r.value or "0"))
        elif r.attribute in ("name", "description", "presence_type", "@ontop"):
            out.append(r)
    return out


def element(rows: list[Row], ref: str) -> tuple[str, list[Row], list[str]]:
    """Return (lccs3 xsi:type, rows in LCCS3 terms, dropped property names)."""
    typ = crosswalk.element_to_lccs3(ref) or ref
    out: list[Row] = []
    dropped: list[str] = []
    for r in rows:
        a = r.attribute
        if a in ("name", "description", "cover", "portioning", "height", "depth", "dynamics", "position",
                 "presence_type") or "/" in a:
            out.append(r)
        elif a == "elementPresenceType":
            out.append(_copy(r, attribute="presence_type",
                             value=crosswalk.PRESENCE_LCHS_TO_LCCS3.get(r.value, "Mandatory")))
        elif a == "heightCM":
            if r.min or r.max:
                out.append(_copy(r, attribute="height", min=_cm_to_m(r.min), max=_cm_to_m(r.max)))
        elif a in WOODY_PHEN:
            if not _unspecified(r):
                out.append(_copy(r, attribute=f"LC_WoodyGrowthLeafPhenology/LC_WoodyLeafPhenology[{WOODY_PHEN[a]}]/percentage"))
        elif a == "deciduousStart":
            if not (r.min, r.max) == ("1", "12"):
                out.append(_copy(r, attribute="LC_WoodyGrowthLeafPhenology/LC_WoodyLeafPhenology[LC_Deciduous]/starting"))
        elif a == "deciduousLength":
            if not (r.min, r.max) == ("1", "12"):
                out.append(_copy(r, attribute="LC_WoodyGrowthLeafPhenology/LC_WoodyLeafPhenology[LC_Deciduous]/length"))
        elif a in WOODY_LEAF:
            if not _unspecified(r):
                out.append(_copy(r, attribute=f"LC_WoodyGrowthLeafType/LC_WoodyLeafType[{WOODY_LEAF[a]}]/percentage"))
        elif a in HERB_PHEN:
            if not _unspecified(r):
                out.append(_copy(r, attribute=f"LC_HerbaceousGrowthLeafPhenology/LC_HerbaceousLeafPhenology[{HERB_PHEN[a]}]/percentage"))
        elif a == "temporalType":
            if r.value:
                out.append(_copy(r, attribute="sequential_temporal_relationship/type",
                                 value=TEMPORAL.get(r.value.lower(), r.value)))
        elif a == "lengthOfTemporalRelationship":
            if not _unspecified(r):
                out.append(_copy(r, attribute="sequential_temporal_relationship/length"))
        elif a in ("woodyLeafPhenology", "woodyLeafType", "herbaceousLeafPhenology", "instanceIndex",
                   "density", "uOMArea", "elementHorizontalSpreading", "lifeFormSpecialization",
                   "lengthOfTemporalRelationshipUnits", "periodVariationType", "periodVariationDescription",
                   "persistencePeriod", "persistenceUnits", "heightCM", "sealed", "macropatternType",
                   "macropatternCoverage", "linearSurfaceType", "elementID", "formElementID", "objectID",
                   "objectReference"):
            if r.value or r.min or r.max:
                dropped.append(a)
        else:
            dropped.append(a)
    # LCCS3 requires a presence type on the element
    if not any(r.attribute == "presence_type" for r in out):
        out.append(Row(**{**rows[0].__dict__, "attribute": "presence_type", "value": "Mandatory", "min": "", "max": ""}))
    return typ, out, dropped


CLASS_CHAR_GROUPS = {
    "geographical_aspects": ("LC_GeographicalAspects", {"type": "type"}),
    "topographical_aspects": ("LC_TopographicalAspects", {"altitude": "altitude", "slopeExposition": "slope_exposition", "slope": "slope"}),
    "climate": ("LC_Climate", {"termalZone": "termal_zone", "lengthOfGrowingPeriod": "length_of_growing_period"}),
    "landform": ("LC_LandForm", {"type": "type", "slopeClassType": "slope_class_type"}),
}


def class_char(rows: list[Row], group: str) -> tuple[str, list[Row]]:
    """LChS class-characteristic group ('topographical_aspects' with 'topographical_aspects-slope'
    fields) -> LCCS3 class characteristic type and rows. Unknown groups return ('', [])."""
    if group not in CLASS_CHAR_GROUPS:
        return "", []
    typ, fields = CLASS_CHAR_GROUPS[group]
    out = []
    for r in rows:
        a = r.attribute
        if a.startswith(group + "-"):
            a = a[len(group) + 1:]
        if a in ("name", "description"):
            out.append(_copy(r, attribute=a))
        elif a in fields and (r.value or r.min or r.max):
            out.append(_copy(r, attribute=fields[a]))
    return typ, out


def characteristic(rows: list[Row], ref: str) -> tuple[str, list[Row], list[str]]:
    vals = {r.attribute: r for r in rows}
    out: list[Row] = []
    dropped: list[str] = []
    typ = crosswalk.char_to_lccs3(ref) or ""
    if ref == "LC_VegetationArtificialityCharacteristic":
        v = (vals.get("vegetationArtificiality").value if "vegetationArtificiality" in vals else "").lower()
        typ = "LC_CultivatedAndManagedVegetation" if "cultiv" in v or "managed" in v else "LC_NaturalOrSeminaturalVegetation"
    elif ref == "LC_CultivatedAndManagedVegetationCharacteristics":
        typ = "LC_CultivatedAndManagedVegetation"
    elif ref == "LC_WaterSalinityCharacteristic":
        typ = "LC_WaterSalinity"
        if "waterSalinity" in vals:
            out.append(_copy(vals["waterSalinity"], attribute="type"))
    elif ref == "LC_ArtificialityCharacteristic":
        typ = "LC_Artificiality"
        if "artificiality" in vals:
            out.append(_copy(vals["artificiality"], attribute="type"))
    elif ref == "LC_WaterChemistryCharacteristic":
        typ = "LC_WaterChemistry"
    if not typ:
        typ = ref
    for r in rows:
        if r.attribute in ("name", "description", "CharacteristicLabel"):
            out.append(_copy(r, attribute="name" if r.attribute == "CharacteristicLabel" else r.attribute))
        elif r.attribute in ("waterSalinity", "artificiality"):
            continue
        elif r.attribute in ("vegetationArtificiality", "instanceIndex", "BlockReference"):
            continue
        elif r.attribute and not any(o.attribute == r.attribute for o in out):
            dropped.append(r.attribute)
    seen = set()
    dedup = []
    for r in out:
        if r.attribute not in seen:
            seen.add(r.attribute)
            dedup.append(r)
    return typ, dedup, dropped
