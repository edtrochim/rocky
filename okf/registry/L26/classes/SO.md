---
id: registry:L26:SO
kind: class
title: SO Shrubs open
system: registry:L26
code: SO
name: Shrubs open
status: registered
decomposed: true
file_class_id: '36'
n_rows: 42
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L26
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
- okf/registry/_raw/L26/L26.lccs
schema: okf/0.1
---

# SO Shrubs open

## Definition (verbatim, FAO LCLR)

Natural shrubs with cover 41-65%. Optional trees (0-15%) and herbs (0-50%).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 5D | 61 Optional | `LC_Tree` | Mandatory | 0.0–15.0 |  | LC_VegetationArtificialityCharacteristic |
| 5D | 5E Mandatory | `LC_Shrub` | Mandatory | 41.0–65.0 |  | LC_VegetationArtificialityCharacteristic |
| 5D | B0 Optional | `LC_HerbaceousGrowthForm` | Mandatory | 0.0–50.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `36`.
