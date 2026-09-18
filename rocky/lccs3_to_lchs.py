"""Property-level mapping from LCCS3-native rows to LChS rows.

Used in two places: when a table read from ``.lccs`` is written as ``.LChS``,
and when the validator normalises LCCS3 rows before checking them against the
LChS vocabulary. Mirrors ``lchs_to_lccs3``. Anything without an LChS home is
returned in ``dropped`` so the caller can report it; nothing is silently lost
from the table itself.
"""

from __future__ import annotations

import re

from .table import Row
from . import crosswalk

_PATH_MAP = {
    "LC_WoodyGrowthLeafPhenology/LC_WoodyLeafPhenology[LC_Evergreen]/percentage": "evergreenPercentage",
    "LC_WoodyGrowthLeafPhenology/LC_WoodyLeafPhenology[LC_Deciduous]/percentage": "deciduousPercentage",
    "LC_WoodyGrowthLeafPhenology/LC_WoodyLeafPhenology[LC_Deciduous]/starting": "deciduousStart",
    "LC_WoodyGrowthLeafPhenology/LC_WoodyLeafPhenology[LC_Deciduous]/length": "deciduousLength",
    "LC_WoodyGrowthLeafType/LC_WoodyLeafType[LC_Broadleaved]/percentage": "broadLeafPercentage",
    "LC_WoodyGrowthLeafType/LC_WoodyLeafType[LC_Needleleaved]/percentage": "needleLeafPercentage",
    "LC_WoodyGrowthLeafType/LC_WoodyLeafType[LC_Aphillous]/percentage": "aphyllousPercentage",
    "LC_HerbaceousGrowthLeafPhenology/LC_HerbaceousLeafPhenology[LC_Perennial]/percentage": "perennialPercentage",
    "LC_HerbaceousGrowthLeafPhenology/LC_HerbaceousLeafPhenology[LC_Annual]/percentage": "nonPerennialPercentage",
    "LC_HerbaceousGrowthLeafPhenology/LC_HerbaceousLeafPhenology[LC_Biennial]/percentage": "nonPerennialPercentage",
    "sequential_temporal_relationship/type": "temporalType",
    "sequential_temporal_relationship/length": "lengthOfTemporalRelationship",
    "LC_WoodyGrowthLeafType/LC_WoodyLeafType[LC_Broadleaved]/arrangement": "leafArragement",
    "LC_WoodyGrowthLeafType/LC_WoodyLeafType[LC_Broadleaved]/shape": "leafShape",
    "LC_WoodyGrowthLeafType/LC_WoodyLeafType[LC_Broadleaved]/venation": "leafVenation",
}
HERBACEOUS = {"LC_HerbaceousGrowthForm", "LC_Graminoid", "LC_Forbs"}


def _copy(r: Row, **kw) -> Row:
    return Row(**{**r.__dict__, **kw})


def _m_to_cm(s: str) -> str:
    try:
        return f"{float(s) * 100:g}"
    except ValueError:
        return s


CLASS_CHAR_TYPES = {
    "LC_GeographicalAspects": ("geographical_aspects", {"type": "type"}),
    "LC_TopographicalAspects": ("topographical_aspects", {"altitude": "altitude", "slope_exposition": "slopeExposition", "slope": "slope"}),
    "LC_Climate": ("climate", {"termal_zone": "termalZone", "length_of_growing_period": "lengthOfGrowingPeriod"}),
    "LC_LandForm": ("landform", {"type": "type", "slope_class_type": "slopeClassType"}),
}


def class_char(rows: list[Row], lccs3_type: str) -> tuple[str, list[Row], list[str]]:
    """LCCS3 class characteristic -> LChS group with prefixed fields; unknown types are dropped."""
    if lccs3_type not in CLASS_CHAR_TYPES:
        return "", [], [r.attribute for r in rows]
    group, fields = CLASS_CHAR_TYPES[lccs3_type]
    out, dropped = [], []
    for r in rows:
        a = r.attribute
        if a in ("name", "description"):
            out.append(_copy(r, ref=group, attribute=f"{group}-{a}"))
        elif a in fields:
            out.append(_copy(r, ref=group, attribute=f"{group}-{fields[a]}"))
        elif a:
            dropped.append(a)
    return group, out, dropped


def hp_rows(rows: list[Row]) -> list[Row]:
    out = []
    for r in rows:
        if r.attribute == "occurance":
            out.append(_copy(r, attribute="occurrence"))
        elif r.attribute in ("name", "description", "type", "cover", "occurrence"):
            out.append(r)
    return out


def stratum_rows(rows: list[Row]) -> list[Row]:
    out = []
    for r in rows:
        if r.attribute == "presence_type":
            out.append(_copy(r, attribute="presenceType", value=crosswalk.PRESENCE_LCCS3_TO_LCHS.get(r.value, r.value)))
        elif r.attribute == "@ontop":
            out.append(_copy(r, attribute="onTop", value="" if r.value in ("0", "") else r.value))
        elif r.attribute in ("name", "description"):
            out.append(r)
    return out


def element(rows: list[Row], lccs3_type: str) -> tuple[str, list[Row], list[str]]:
    """Return (LChS BlockReference, rows in LChS terms, dropped attribute paths)."""
    ref, _note = crosswalk.element_to_lchs(lccs3_type)
    out: list[Row] = []
    dropped: list[str] = []
    for r in rows:
        a = r.attribute
        if a == "lccs3_type":
            continue
        if a == "presence_type":
            out.append(_copy(r, attribute="elementPresenceType",
                             value=crosswalk.PRESENCE_LCCS3_TO_LCHS.get(r.value, r.value)))
        elif a == "height" and ref in HERBACEOUS:
            out.append(_copy(r, attribute="heightCM", min=_m_to_cm(r.min), max=_m_to_cm(r.max)))
        elif a in ("name", "description", "cover", "portioning", "height", "depth", "dynamics", "position"):
            out.append(r)
        elif a in _PATH_MAP:
            out.append(_copy(r, attribute=_PATH_MAP[a]))
        elif a in ("LC_WoodyGrowthLeafPhenology", "LC_WoodyGrowthLeafType", "LC_HerbaceousGrowthLeafPhenology",
                   "sequential_temporal_relationship") or re.match(r".*\[LC_\w+\]$", a):
            continue  # container rows with no value of their own
        else:
            dropped.append(a)
    if lccs3_type in ("LC_Road", "LC_Railway", "LC_CommunicationsAndOther"):
        out.append(Row(**{**rows[0].__dict__, "attribute": "linearSurfaceType", "value": lccs3_type[3:], "min": "", "max": ""}))
    return ref, out, dropped


def characteristic(rows: list[Row], lccs3_type: str) -> tuple[str, list[Row], list[str]]:
    ref, _note = crosswalk.char_to_lchs(lccs3_type)
    out: list[Row] = []
    dropped: list[str] = []
    for r in rows:
        a = r.attribute
        if a == "lccs3_type":
            continue
        if a in ("name", "description"):
            out.append(r)
        elif lccs3_type == "LC_WaterSalinity" and a == "type":
            out.append(_copy(r, attribute="waterSalinity"))
        elif lccs3_type == "LC_Artificiality" and a == "type":
            out.append(_copy(r, attribute="artificiality"))
        elif lccs3_type in ("LC_NaturalOrSeminaturalVegetation", "LC_CultivatedAndManagedVegetation") and a == "":
            continue
        else:
            dropped.append(a)
    if lccs3_type == "LC_NaturalOrSeminaturalVegetation":
        out.append(Row(**{**rows[0].__dict__, "attribute": "vegetationArtificiality", "value": "Natural or Seminatural", "min": "", "max": ""}))
    elif lccs3_type in ("LC_CultivatedAndManagedVegetation", "LC_UrbanPark") and ref == "LC_VegetationArtificialityCharacteristic":
        out.append(Row(**{**rows[0].__dict__, "attribute": "vegetationArtificiality", "value": "Cultivated", "min": "", "max": ""}))
    return ref, out, dropped
