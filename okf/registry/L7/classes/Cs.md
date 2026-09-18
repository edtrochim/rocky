---
id: registry:L7:Cs
kind: class
title: Cs Closed Shrub Dominated
system: registry:L7
code: Cs
name: Closed Shrub Dominated
status: registered
decomposed: true
file_class_id: 1E
n_rows: 40
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L7
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
- okf/registry/_raw/L7/L7.lccs
schema: okf/0.1
---

# Cs Closed Shrub Dominated

## Definition (verbatim, FAO LCLR)

Closed natural shrubs (>80%). The shrub foliage can be either evergreen or deciduous.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1F | 20 Mandatory | `LC_Shrub` | Mandatory | 80.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 1F | 23 Mandatory | `LC_Tree` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 1F | 26 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `1E`.
