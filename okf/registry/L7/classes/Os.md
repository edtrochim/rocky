---
id: registry:L7:Os
kind: class
title: Os Open Shrub Dominated
system: registry:L7
code: Os
name: Open Shrub Dominated
status: registered
decomposed: true
file_class_id: '29'
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

# Os Open Shrub Dominated

## Definition (verbatim, FAO LCLR)

Open natural shrubs (20-80%). The shrub foliage can be either evergreen or deciduous.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2A | 31 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 2A | 2B Mandatory | `LC_Shrub` | Mandatory | 20.0–80.0 |  | LC_VegetationArtificialityCharacteristic |
| 2A | 2E Mandatory | `LC_Tree` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `29`.
