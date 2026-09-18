---
id: registry:L5:TOP
kind: class
title: TOP Trees sparse natural vegetation
system: registry:L5
code: TOP
name: Trees sparse natural vegetation
status: registered
decomposed: true
file_class_id: 1C
n_rows: 33
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L5
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L5/L5.lccs
schema: okf/0.1
---

# TOP Trees sparse natural vegetation

## Definition (verbatim, FAO LCLR)

Natural open trees, occasionally with sparse or closed her-baceous vegetation cover, with percent-age cover varying from 10 to 60%.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1D | 23 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 1D | 1E Mandatory | `LC_Tree` | Mandatory | 10.0–60.0 | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/name=Evergreen; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/description=Describe an Evergreen leaf phenology element | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `1C`.
