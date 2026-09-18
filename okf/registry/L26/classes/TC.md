---
id: registry:L26:TC
kind: class
title: TC Trees close
system: registry:L26
code: TC
name: Trees close
status: registered
decomposed: true
file_class_id: '91'
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

# TC Trees close

## Definition (verbatim, FAO LCLR)

Natural trees with cover 66-100% with a layer of herbs (0-50%). Optional shrubs (0-15%).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 92 | 93 Mandatory | `LC_Tree` | Mandatory | 66.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 92 | 96 Optional | `LC_Shrub` | Mandatory | 0.0–15.0 |  | LC_VegetationArtificialityCharacteristic |
| 92 | 99 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 0.0–50.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `91`.
