---
id: registry:L20:He_pa
kind: class
title: He_pa Grassland with scattered palm trees
system: registry:L20
code: He_pa
name: Grassland with scattered palm trees
status: registered
decomposed: true
file_class_id: '68'
n_rows: 39
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L20
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L20/L20.lccs
schema: okf/0.1
---

# He_pa Grassland with scattered palm trees

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 69 | 6A Mandatory | `LC_Tree` | Mandatory | 1.0–15.0 | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/name=Evergreen; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/description=Describe an Evergreen leaf phenology element; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/name=Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/description=Contains the elements of Woody Growth Leaf Type | LC_VegetationArtificialityCharacteristic |
| 69 | 6D Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 0.0–99.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `68`.
