---
id: registry:L21:D
kind: class
title: D Deciduous forest
system: registry:L21
code: D
name: Deciduous forest
status: registered
decomposed: true
file_class_id: 1B
n_rows: 59
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

# D Deciduous forest

## Definition (verbatim, FAO LCLR)

Comprised of dry mixed deciduous forest and dry Dipterocarp forests.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1C | 20 Optional | `LC_Shrub` | Mandatory | 0.0–10.0 |  | LC_VegetationArtificialityCharacteristic |
| 1C | 23 Mandatory | `LC_Tree` | Mandatory | 10.0–100.0 | height 5.0–15.0 | LC_VegetationArtificialityCharacteristic |
| 1C | 23 Mandatory | `LC_Tree` | Optional |  | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/name=Evergreen; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/description=Describe an Evergreen leaf phenology element; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/name=Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/description=Contains the elements of Woody Growth Leaf Type | LC_VegetationArtificialityCharacteristic |
| 1C | 1D Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 5.0–70.0 | height 1.0–3.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `1B`.
