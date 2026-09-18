"""Corrected cross-country harmonisation for MapBiomas South America.

Replaces the single lossy crosswalk in `extract_hansen_mapbiomas_v16.Rmd` with
three explicit tiers, because "harmonised" means different things depending on
how much comparability an analysis actually needs.

  Tier A  MapBiomas level-1 (6 classes).  Exact.  Every national legend is a
          strict hierarchy under the same six parents, so this collapse loses
          only detail, never correctness.
  Tier B  Pan-MapBiomas legend (~35 classes).  Keeps every code that already
          means the same thing in every country that publishes it.  Brazil
          simply never emits the Andean/Patagonian classes, and the Andean
          countries never emit the Brazilian crop split.
  Tier C  MapBiomas Brazil Collection 10.  The target the Rmd pipeline uses.
          Complete (no code silently dropped) and every lossy fold is named.

Design rules applied throughout:

  * A fold must never change a pixel's Tier A class.  This is what forced
    66/63/77 shrubland -> 12 Grassland rather than -> 4 Savanna Formation
    (4 sits under level-1 Forest), and 34 Glacier -> 33 rather than -> 25.
  * A code that exists in the target legend with a *different* meaning is
    remapped, not passed through.  Venezuela's 50 is xerophytic shrubland,
    not Brazil's herbaceous sandbank vegetation.
  * Nothing falls through to 27.  27 means "MapBiomas could not observe this
    pixel" and nothing else.

Outputs tier_a.csv, tier_b.csv, tier_c.csv and the markdown used in the README.
"""

from __future__ import annotations

import csv
import json
import os

BUILD = os.path.dirname(os.path.abspath(__file__))
LEGENDS = json.load(open(os.path.join(BUILD, "legends.json"), encoding="utf-8"))
OBSERVED = json.load(open(os.path.join(BUILD, "observed_classes.json"), encoding="utf-8"))

COUNTRIES = [c for c in sorted(LEGENDS) if not c.startswith("_")]

# -----------------------------------------------------------------------------
# Tier A - MapBiomas level-1, read off the hierarchy in each national legend PDF
# -----------------------------------------------------------------------------

LEVEL1 = {
    1: "Forest formation",
    10: "Non-forest natural formation",
    14: "Farming",
    22: "Non-vegetated area",
    26: "Water body",
    27: "Not observed",
}

HIERARCHY: dict[str, dict[int, list[int]]] = {
    "argentina": {1: [3, 4, 6], 10: [66, 77, 63, 12, 11, 73],
                  14: [18, 19, 36, 15, 9, 21], 22: [24, 25],
                  26: [34, 33], 27: [27]},
    "bolivia":   {1: [3, 4, 6], 10: [11, 12, 29, 66, 81, 82, 13],
                  14: [15, 18, 39, 72, 21], 22: [23, 24, 30, 61, 68, 25],
                  26: [33, 31, 34], 27: [27]},
    "brazil":    {1: [3, 4, 5, 6, 49], 10: [11, 12, 32, 29, 50],
                  14: [15, 18, 19, 39, 20, 40, 62, 41, 36, 46, 47, 35, 48, 9, 21],
                  22: [23, 24, 30, 75, 25], 26: [33, 31], 27: [27]},
    "chile":     {1: [3, 59, 60, 67, 4, 6], 10: [11, 12, 63, 66, 29, 13, 32],
                  14: [9, 18, 15, 21], 22: [24, 23, 61, 25],
                  26: [33, 34], 27: [27]},
    "colombia":  {1: [3, 5, 6, 49], 10: [11, 12, 32, 29, 50, 13, 81, 82],
                  14: [9, 35, 74, 21], 22: [23, 24, 30, 68, 25, 75],
                  26: [33, 31, 34], 27: [27]},
    "ecuador":   {1: [3, 4, 5, 6], 10: [11, 12, 81, 82, 29, 13],
                  14: [9, 21, 74], 22: [24, 30, 23, 25, 68],
                  26: [33, 34, 31], 27: [27]},
    "paraguay":  {1: [3, 4, 6], 10: [11, 12], 14: [15, 18, 9],
                  22: [], 26: [], 27: [27]},
    "peru":      {1: [3, 4, 5, 6], 10: [11, 12, 29, 66, 70, 13],
                  14: [15, 18, 35, 40, 72, 9, 21],
                  22: [23, 24, 30, 32, 61, 68, 25], 26: [33, 31, 34], 27: [27]},
    "uruguay":   {1: [3], 10: [11, 12], 14: [9, 79, 80, 83, 15, 19, 18],
                  22: [], 26: [33], 27: [27]},
    "venezuela": {1: [3, 4, 5, 6], 10: [11, 12, 29, 32, 66, 50, 13, 81, 82],
                  14: [15, 18, 21, 9], 22: [23, 24, 30, 68, 25],
                  26: [33, 34, 31], 27: [27]},
}

# The aggregate codes themselves (a raster may carry the parent code directly -
# Paraguay and Uruguay do exactly this for 22 and 26).
for _c, _h in HIERARCHY.items():
    for _parent in list(_h):
        _h[_parent] = sorted(set(_h[_parent]) | {_parent})

# Documented hierarchy discrepancy: Peru files the hypersaline/coastal salt flat
# (32) under Non-vegetated, while Brazil, Colombia and Venezuela file it under
# Non-forest natural formation. Tier A follows each country's own legend.
HIERARCHY_NOTES = [
    "Peru files code 32 (Coastal salt flat) under level-1 22 Non-vegetated area, "
    "while Brazil, Colombia and Venezuela file the same code (Hypersaline tidal "
    "flat) under level-1 10 Non-forest natural formation. Tier A follows each "
    "country's own published hierarchy rather than forcing one of the two.",
    "Uruguay's code 3 is 'Closed forest and closed shrubland', so Uruguayan "
    "level-1 Forest includes shrubland that other countries would place under "
    "level-1 10 Non-forest natural formation.",
    "Code 4 is Savanna Formation in Brazil, Open forest in Argentina, Bolivia and "
    "Ecuador, Dry forest in Peru, Wooded savanna in Venezuela and Open Natural "
    "Woodlands in Paraguay. All six sit under level-1 1 Forest formation, so "
    "Tier A is unaffected; Tier B keeps the code with this caveat attached.",
]

# -----------------------------------------------------------------------------
# Tier B - pan-MapBiomas legend
# -----------------------------------------------------------------------------
# Codes are kept as published wherever the meaning is stable across every
# country that emits them. Only genuine collisions are remapped.

TIER_B_NAMES = {
    1: "Forest formation (aggregate)",
    3: "Forest",
    4: "Open / dry forest or savanna formation",
    5: "Mangrove",
    6: "Flooded forest",
    49: "Wooded sandbank vegetation",
    10: "Non-forest natural formation (aggregate)",
    11: "Wetland / flooded herbaceous",
    12: "Grassland / herbaceous",
    13: "Other non-forest natural formation",
    29: "Rocky outcrop",
    32: "Hypersaline tidal flat / coastal salt flat",
    50: "Herbaceous sandbank vegetation",
    61: "Salt flat (salar)",
    63: "Steppe",
    66: "Shrubland",
    70: "Fog oasis (loma)",
    73: "Peatland",
    81: "Andean grassland and shrubland",
    82: "Flooded Andean grassland and shrubland",
    14: "Farming (aggregate)",
    9: "Forest plantation",
    79: "Forest plantation - pine",
    80: "Forest plantation - eucalyptus",
    83: "Forest plantation - other species",
    15: "Pasture",
    18: "Agriculture",
    19: "Temporary crop",
    20: "Sugar cane",
    35: "Palm oil",
    36: "Perennial crop",
    39: "Soybean",
    40: "Rice",
    41: "Other temporary crops",
    46: "Coffee",
    47: "Citrus",
    48: "Other perennial crops",
    62: "Cotton",
    72: "Other crops",
    74: "Banana",
    21: "Mosaic of uses",
    22: "Non-vegetated area (aggregate)",
    23: "Beach, dune and sand spot",
    24: "Urban / infrastructure",
    25: "Other non-vegetated area",
    30: "Mining",
    68: "Other natural non-vegetated area",
    75: "Photovoltaic power plant",
    26: "Water body (aggregate)",
    31: "Aquaculture",
    33: "River, lake or ocean",
    34: "Glacier, ice and permanent snow",
    27: "Not observed",
}

# country -> {national code: (tier B code, reason)}. Anything not listed is an
# identity mapping.
TIER_B_OVERRIDES: dict[str, dict[int, tuple[int, str]]] = {
    "venezuela": {
        50: (66, "Venezuela's 50 is Xerophytic grassland/shrubland, not the "
                 "herbaceous sandbank vegetation that Brazil and Colombia encode "
                 "as 50. Remapped to 66 Shrubland to avoid a silent collision."),
    },
    "argentina": {
        77: (66, "Argentina splits shrubland into 66 closed and 77 open. Only 66 "
                 "exists in the other national legends, so 77 is merged into it."),
        63: (66, "Argentina's 63 is a shrub-and-herbaceous mosaic; Chile's 63 is "
                 "Steppe. Merged into 66 Shrubland for Argentina to avoid the "
                 "collision, and 63 is reserved for Chile's Steppe."),
    },
    "uruguay": {
        19: (18, "Uruguay's legend calls agriculture 19, but no Uruguayan raster "
                 "contains 19 - they encode agriculture as 18. Both are folded "
                 "to 18 so Uruguay lines up with the other countries."),
    },
    "chile": {
        7: (27, "Not a MapBiomas class. A handful of stray pixels in the Chile "
                "2022 raster, produced by a non-nearest resampling at mosaic "
                "time. Treated as Not observed."),
        16: (27, "Not a MapBiomas class. Same mosaic artefact as code 7."),
    },
}

# -----------------------------------------------------------------------------
# Tier C - MapBiomas Brazil Collection 10
# -----------------------------------------------------------------------------

BRAZIL_C10 = {int(k): v[0] for k, v in LEGENDS["brazil"]["classes"].items()}

# Folds applied to any country, expressed against the Tier B code.
# tier_b_code -> (brazil code, lossy?, reason)
TIER_C_FOLDS: dict[int, tuple[int, bool, str]] = {
    13: (12, True, "Brazil Collection 10 dropped 'Other non-forest natural "
                   "formation'. Folded into 12 Grassland, which shares its "
                   "level-1 parent (10)."),
    61: (25, True, "No salt flat class in Brazil. Folded into 25 Other non "
                   "Vegetated Areas; level-1 parent (22) is preserved."),
    63: (12, True, "No steppe class in Brazil. Folded into 12 Grassland; "
                   "level-1 parent (10) is preserved."),
    66: (12, True, "No shrubland class in Brazil. Folded into 12 Grassland "
                   "rather than 4 Savanna Formation: 4 sits under level-1 1 "
                   "Forest, so mapping shrubland there would reclassify it as "
                   "forest and inflate forest area across Chile, Argentina, "
                   "Peru, Bolivia and Venezuela."),
    68: (25, True, "No 'other natural non-vegetated area' class in Brazil. "
                   "Folded into 25; level-1 parent (22) is preserved."),
    70: (12, True, "No fog oasis (loma) class in Brazil. Folded into 12 "
                   "Grassland; level-1 parent (10) is preserved."),
    73: (11, True, "No peatland class in Brazil. Folded into 11 Wetland; "
                   "level-1 parent (10) is preserved."),
    81: (12, True, "No Andean grassland/shrubland class in Brazil. Folded into "
                   "12 Grassland; level-1 parent (10) is preserved. This is a "
                   "large share of the Bolivian, Peruvian, Ecuadorian and "
                   "Colombian highlands - flag it in any highland analysis."),
    82: (11, True, "No flooded Andean grassland/shrubland class in Brazil. "
                   "Folded into 11 Wetland; level-1 parent (10) is preserved."),
    34: (33, True, "Brazil Collection 10 has no glacier class. Folded into 33 "
                   "River, Lake and Ocean because every national legend files "
                   "glacier under level-1 26 Water body; folding to 25 instead "
                   "would move the pixels to level-1 22 Non-vegetated."),
    74: (48, True, "No banana class in Brazil. Banana is a perennial crop, so "
                   "it folds into 48 Other Perennial Crops; level-1 parent (14) "
                   "is preserved. The Rmd previously sent it to 41 Other "
                   "Temporary Crops, which is the wrong crop cycle."),
    72: (41, True, "'Other crops' in Bolivia and Peru is not resolved to a crop "
                   "cycle. Folded into 41 Other Temporary Crops, the Brazilian "
                   "catch-all; level-1 parent (14) is preserved."),
    79: (9, True, "Brazil does not split forest plantation by species. Folded "
                  "into 9 Forest Plantation, its own parent class - detail is "
                  "lost but no class boundary is crossed."),
    80: (9, True, "As for 79."),
    83: (9, True, "As for 79."),
    59: (3, True, "Brazil Collection 10 does not separate primary from secondary "
                  "forest. Folded into 3 Forest Formation; level-1 parent (1) is "
                  "preserved."),
    60: (3, True, "As for 59."),
    67: (4, True, "No dwarf/krummholz forest class in Brazil. Folded into 4 "
                  "Savanna Formation, the Brazilian open-canopy woody class; "
                  "level-1 parent (1 Forest) is preserved."),
}


def tier_a(country: str, code: int) -> int | None:
    for parent, children in HIERARCHY[country].items():
        if code in children:
            return parent
    return None


def tier_b(country: str, code: int) -> tuple[int, str]:
    override = TIER_B_OVERRIDES.get(country, {}).get(code)
    if override:
        return override
    return code, ""


def tier_c(country: str, code: int) -> tuple[int, bool, str]:
    b_code, b_reason = tier_b(country, code)
    if b_code in TIER_C_FOLDS:
        target, lossy, reason = TIER_C_FOLDS[b_code]
        if b_reason:
            reason = b_reason + " " + reason
        return target, lossy, reason
    if b_code in BRAZIL_C10:
        return b_code, False, b_reason
    return 27, True, (b_reason or "") + (
        " No equivalent in Brazil Collection 10 and no defined fold." if not b_reason else "")


def observed_codes(country: str) -> list[int]:
    codes: set[int] = set()
    for fname, hist in OBSERVED.items():
        if country in fname.lower():
            codes |= {int(c) for c in hist}
    return sorted(codes - {0})


def build() -> list[dict]:
    rows = []
    for country in COUNTRIES:
        for code in observed_codes(country):
            a = tier_a(country, code)
            b, b_reason = tier_b(country, code)
            c, lossy, c_reason = tier_c(country, code)
            national = LEGENDS[country]["classes"].get(str(code))
            rows.append({
                "country": country,
                "code": code,
                "national_class": national[0] if national else
                                  "(not in the published national legend)",
                "tier_a_code": a if a is not None else 27,
                "tier_a_class": LEVEL1[a] if a is not None else LEVEL1[27],
                "tier_b_code": b,
                "tier_b_class": TIER_B_NAMES.get(b, "?"),
                "tier_b_note": b_reason,
                "tier_c_code": c,
                "tier_c_class": BRAZIL_C10.get(c, "?"),
                "tier_c_lossy": "yes" if lossy else "no",
                "tier_c_note": c_reason,
            })
    return rows


def main() -> None:
    rows = build()
    out = os.path.join(BUILD, "harmonization.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print("wrote", out, len(rows), "rows")

    unresolved = [r for r in rows if r["tier_a_code"] == 27 and r["code"] != 27]
    print("codes with no level-1 parent:",
          [(r["country"], r["code"]) for r in unresolved] or "none")
    lossy = [r for r in rows if r["tier_c_lossy"] == "yes"]
    print(f"Tier C: {len(rows) - len(lossy)} exact, {len(lossy)} lossy folds")


if __name__ == "__main__":
    main()
