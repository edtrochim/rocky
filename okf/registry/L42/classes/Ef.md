---
id: registry:L42:Ef
kind: class
title: Ef Evergreen forest
system: registry:L42
code: Ef
name: Evergreen forest
status: registered
decomposed: true
file_class_id: '2'
n_rows: 24
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L42
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L42/L42.lccs
schema: okf/0.1
---

# Ef Evergreen forest

## Definition (verbatim, FAO LCLR)

An evergreen forest is a type of forest where the majority of the trees retain their leaves throughout the year, regardless of seasonal changes. These forests are characterized by their lush, dense foliage that remains green year-round

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3 | 4 Mandatory | `LC_Tree` | Mandatory | 70.0–100.0 | portioning 10.0–100.0; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/name=Evergreen; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/description=Describe an Evergreen leaf phenology element; height 5.0–30.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `2`.
