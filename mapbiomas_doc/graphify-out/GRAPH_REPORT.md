# Graph Report - mapbiomas_doc  (2026-09-17)

## Corpus Check
- Corpus is ~14,346 words - fits in a single context window. You may not need a graph.

## Summary
- 190 nodes · 631 edges · 8 communities
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 69 edges (avg confidence: 0.84)
- Token cost: 200,000 input · 35,474 output

## Community Hubs (Navigation)
- Catalog Guide & Original Rmd Crosswalk Audit
- Tier C Lossy Folds into Brazil C10
- Code 50 Collision & Passthrough Flaw
- Tier A Level-1 Hierarchy & Caveats
- Tier B Collision Resolutions (Shrubland)
- Chile Forest Classes & Artefacts
- COG Processing & Provenance Files
- Fold Rules & Trazo Fields Pipeline

## God Nodes (most connected - your core abstractions)
1. `Tier B - pan-MapBiomas legend (~50 classes)` - 29 edges
2. `MapBiomas Chile` - 29 edges
3. `Rule: no code falls through to 27 Not observed` - 27 edges
4. `MapBiomas Brazil Collection 10` - 27 edges
5. `Rule: no fold may change a pixel's Tier A class` - 26 edges
6. `MapBiomas Bolivia` - 24 edges
7. `MapBiomas South America COG catalog (source.coop)` - 22 edges
8. `crosswalk.csv (original Rmd crosswalk with audit column)` - 21 edges
9. `MapBiomas Peru` - 20 edges
10. `MapBiomas Venezuela` - 19 edges

## Surprising Connections (you probably didn't know these)
- `Rule: no code falls through to 27 Not observed` --rationale_for--> `tier_c()`  [INFERRED]
  README.md → provenance/harmonization.py
- `TIER_B_NAMES (pan-MapBiomas legend, ~50 named codes)` --implements--> `Tier B - pan-MapBiomas legend (~50 classes)`  [EXTRACTED]
  provenance/harmonization.py → README.md
- `Flaw: silent drops to 27 Not Observed` --rationale_for--> `Rule: no code falls through to 27 Not observed`  [INFERRED]
  provenance/crosswalk.py → README.md
- `Rule: no code falls through to 27 Not observed` --conceptually_related_to--> `Chile stray codes 7 and 16 -> 27`  [INFERRED]
  README.md → provenance/harmonization.py
- `Fold 59/60 primary/secondary -> 3, 67 dwarf forest -> 4` --references--> `MapBiomas Chile`  [INFERRED]
  provenance/harmonization.py → README.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Six level-1 parent classes form Tier A** — readme_level1_1_forest_formation, readme_level1_10_non_forest_natural_formation, readme_level1_14_farming, readme_level1_22_non_vegetated_area, readme_level1_26_water_body, readme_level1_27_not_observed, readme_tier_a [EXTRACTED 1.00]
- **Lossy Tier C folds into Brazil C10 12 Grassland** — readme_class_13_other_non_forest_natural_formation, readme_class_63_steppe, readme_class_66_shrubland, readme_class_70_fog_oasis, readme_class_81_andean_grassland_shrubland, readme_brazil_c10_12_grassland [EXTRACTED 1.00]
- **Countries whose rasters are Collection 3** — readme_colombia, readme_ecuador, readme_peru, readme_uruguay, readme_venezuela, readme_bolivia, readme_mapbiomas_collection_3 [EXTRACTED 1.00]
- **Three-tier harmonisation strategy** — readme_tier_a, readme_tier_b, readme_tier_c, readme_harmonization_csv [EXTRACTED 1.00]
- **Catalog build order of operations** — provenance_reproduce_make_cogs, provenance_reproduce_relayout, provenance_harmonization, provenance_reproduce_portolan_add, provenance_reproduce_write_metadata, provenance_reproduce_finalize_stac, provenance_reproduce_make_thumbnails, provenance_reproduce_fix_versions_freshness, provenance_reproduce_register_extra_assets, provenance_reproduce_portolan_readme, provenance_reproduce_portolan_check [EXTRACTED 1.00]
- **Design rules applied throughout harmonization.py** — readme_rule_preserve_tier_a, provenance_harmonization_rule_remap_not_passthrough, readme_rule_no_fallthrough_to_27, provenance_harmonization [EXTRACTED 1.00]

## Communities (8 total, 0 thin omitted)

### Community 0 - "Catalog Guide & Original Rmd Crosswalk Audit"
Cohesion: 0.10
Nodes (43): AGENTS.md (agent guide to the catalog), Availability check: some declared rasters return 404, Catalog is a mirror: MapBiomas produces and licenses, Source Cooperative serves, Per-collection legend sizes (AR 21, BO 30, BR 38, CL 29, CO 31, EC 27, PY 14, PE 33, UY 17, VE 31), Portolan profile v0.1.2 conformance (validated with rashid 0.1.7), Hazard: the same integer means different things in different countries, Self-describing COGs: embedded colour table and CLASS_<code> TIFF tags, BRAZIL (Brazil C10 legend dict) (+35 more)

### Community 1 - "Tier C Lossy Folds into Brazil C10"
Cohesion: 0.18
Nodes (37): Bolivia 13 Other non-forest -> 3 Forest (Rmd error), MapBiomas Bolivia, Brazil C10 11 Wetland, Brazil C10 12 Grassland, Brazil C10 41 Other Temporary Crops, Brazil C10 48 Other Perennial Crops, Brazil C10 9 Forest Plantation, Caveat: never compare raw codes across collections (+29 more)

### Community 2 - "Code 50 Collision & Passthrough Flaw"
Cohesion: 0.17
Nodes (26): Code 50: Herbaceous Sandbank Vegetation (Brazil) vs Xerophytic grassland (Venezuela), Venezuela 50 Xerophytic grassland passed through as Herbaceous Sandbank Vegetation, Flaw: Colombia/Venezuela passthrough, RCL (per-country reclassification tables transcribed from the Rmd), Venezuela 50 -> 66 Shrubland, Rule: a code with a different meaning in the target legend is remapped, not passed through, Availability: 41 of 59 COGs declared but missing (HTTP 404), tools/availability.py (+18 more)

### Community 3 - "Tier A Level-1 Hierarchy & Caveats"
Cohesion: 0.14
Nodes (22): Code 4: Savanna Formation (Brazil) vs Open forests (Argentina), HIERARCHY (per-country level-1 parent -> child codes), HIERARCHY_NOTES (documented hierarchy discrepancies), LEVEL1 (six MapBiomas level-1 classes: 1,10,14,22,26,27), tier_a(), Brazil C10 25 Other non Vegetated Areas, Brazil C10 33 River, Lake and Ocean, Caveat: Peru 32 under 22 vs Brazil/Colombia/Venezuela 32 under 10 (+14 more)

### Community 4 - "Tier B Collision Resolutions (Shrubland)"
Cohesion: 0.18
Nodes (17): Code 63: Shrub and herbaceous mosaic (Argentina) vs Steppe (Chile), Argentina 63 shrub/herbaceous mosaic -> 66, Argentina 77 open shrubland -> 66, Chile stray codes 7 and 16 -> 27, Uruguay 19 -> 18 Agriculture, TIER_B_OVERRIDES (Tier B collision-resolution table), MapBiomas Argentina, 66 Shrubland (+9 more)

### Community 5 - "Chile Forest Classes & Artefacts"
Cohesion: 0.27
Nodes (15): Brazil C10 3 Forest Formation, Brazil C10 4 Savanna Formation, Caveat: Chile 2022 mosaic artefacts (4, 6, 7, 13, 16, 32), Caveat: Chile rasters carry 4, 6, 13, 21, 32 absent from Chile legends, MapBiomas Chile, 27 Not observed, 59 Primary Forest (Chile), 60 Secondary Forest (Chile) (+7 more)

### Community 6 - "COG Processing & Provenance Files"
Cohesion: 0.13
Nodes (15): Caveat: Paraguay legend colours class 9 as #ffefc3, CLASS_<code> TIFF tags, Official MapBiomas colour table per country, COG conversion of MapBiomas exports, Overview resampling = mode (deviation from Portolan nearest), nodata = 0, Provenance tags (MAPBIOMAS_COUNTRY, _YEAR, _COLLECTION, _LEGEND_SOURCE, SOURCE_FILE, OVERVIEW_RESAMPLING), Data type uint8 (lossless cast) (+7 more)

### Community 7 - "Fold Rules & Trazo Fields Pipeline"
Cohesion: 0.27
Nodes (13): Fold 13 / 63 Steppe / 70 Fog oasis -> 12 Grassland, Fold 34 Glacier -> 33 River/Lake/Ocean (not 25), Fold 59/60 primary/secondary -> 3, 67 dwarf forest -> 4, Fold 61 Salt flat / 68 other natural non-veg -> 25, Fold 66 Shrubland -> 12 Grassland (not 4 Savanna), Fold 73 Peatland -> 11 Wetland; 72 Other crops -> 41, Fold 74 Banana -> 48 Other Perennial Crops, Fold 79/80/83 plantation species -> 9 Forest Plantation (+5 more)

## Ambiguous Edges - Review These
- `66 Shrubland` → `67 Dwarf forest (Chile)`  [AMBIGUOUS]
  README.md · relation: semantically_similar_to

## Knowledge Gaps
- **5 isolated node(s):** `source.coop (tristangruppwri/mapbiomas)`, `Tristan Grupp / WRI (republisher)`, `Provenance tags (MAPBIOMAS_COUNTRY, _YEAR, _COLLECTION, _LEGEND_SOURCE, SOURCE_FILE, OVERVIEW_RESAMPLING)`, `tools/availability.py`, `Availability check: some declared rasters return 404`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 9 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `66 Shrubland` and `67 Dwarf forest (Chile)`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **Why does `MapBiomas South America COG catalog (source.coop)` connect `Code 50 Collision & Passthrough Flaw` to `Catalog Guide & Original Rmd Crosswalk Audit`, `Tier C Lossy Folds into Brazil C10`, `Tier A Level-1 Hierarchy & Caveats`, `Tier B Collision Resolutions (Shrubland)`, `Chile Forest Classes & Artefacts`, `COG Processing & Provenance Files`, `Fold Rules & Trazo Fields Pipeline`?**
  _High betweenness centrality (0.140) - this node is a cross-community bridge._
- **Why does `crosswalk.csv (original Rmd crosswalk with audit column)` connect `Catalog Guide & Original Rmd Crosswalk Audit` to `Tier C Lossy Folds into Brazil C10`, `Code 50 Collision & Passthrough Flaw`, `Tier A Level-1 Hierarchy & Caveats`, `Tier B Collision Resolutions (Shrubland)`, `Chile Forest Classes & Artefacts`?**
  _High betweenness centrality (0.115) - this node is a cross-community bridge._
- **Why does `MapBiomas Brazil Collection 10` connect `Fold Rules & Trazo Fields Pipeline` to `Catalog Guide & Original Rmd Crosswalk Audit`, `Tier C Lossy Folds into Brazil C10`, `Code 50 Collision & Passthrough Flaw`, `Tier A Level-1 Hierarchy & Caveats`, `Chile Forest Classes & Artefacts`?**
  _High betweenness centrality (0.109) - this node is a cross-community bridge._
- **Are the 23 inferred relationships involving `Rule: no code falls through to 27 Not observed` (e.g. with `Flaw: silent drops to 27 Not Observed` and `Chile stray codes 7 and 16 -> 27`) actually correct?**
  _`Rule: no code falls through to 27 Not observed` has 23 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Rule: no fold may change a pixel's Tier A class` (e.g. with `Bolivia 13 Other non-forest -> 3 Forest (Rmd error)` and `Rmd folds 66/77/67 shrubland to 4 Savanna Formation (Argentina, Chile)`) actually correct?**
  _`Rule: no fold may change a pixel's Tier A class` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `source.coop (tristangruppwri/mapbiomas)`, `Tristan Grupp / WRI (republisher)`, `Provenance tags (MAPBIOMAS_COUNTRY, _YEAR, _COLLECTION, _LEGEND_SOURCE, SOURCE_FILE, OVERVIEW_RESAMPLING)` to the rest of the system?**
  _5 weakly-connected nodes found - possible documentation gaps or missing edges._