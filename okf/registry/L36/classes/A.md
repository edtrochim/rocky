---
id: registry:L36:A
kind: class
title: A Forest
system: registry:L36
code: A
name: Forest
status: registered
decomposed: true
file_class_id: 15D
n_rows: 50
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L36
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
- okf/registry/_raw/L36/L36.lccs
schema: okf/0.1
---

# A Forest

## Definition (verbatim, FAO LCLR)

The land is primarily covered by desnse natural forests with the presence of bushes and shrubs also possible.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 15E | 15F Mandatory | `LC_Tree` | Mandatory | 10.0–100.0 | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/name=Evergreen; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/description=Describe an Evergreen leaf phenology element; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/percentage 75.0–100.0; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/name=Woody Growth Leaf Type | LC_VegetationArtificialityCharacteristic |
| 15E | 1EF Optional | `LC_Shrub` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 15E | 1F2 Optional | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `15D`.
