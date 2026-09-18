---
id: registry:L21:P
kind: class
title: P Pine forest
system: registry:L21
code: P
name: Pine forest
status: registered
decomposed: true
file_class_id: 9B
n_rows: 52
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L21
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L21/L21.lccs
schema: okf/0.1
---

# P Pine forest

## Definition (verbatim, FAO LCLR)

The area dominated by coniferous trees.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 9C | 9D Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 0.0–15.0 |  | LC_VegetationArtificialityCharacteristic |
| 9C | A0 Optional | `LC_Shrub` | Mandatory | 0.0–15.0 |  | LC_VegetationArtificialityCharacteristic |
| 9C | A3 Mandatory | `LC_Tree` | Mandatory | 65.0–100.0 | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/name=Evergreen; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/description=Describe an Evergreen leaf phenology element; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/percentage 100.0–100.0; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/name=Woody Growth Leaf Type | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `9B`.
