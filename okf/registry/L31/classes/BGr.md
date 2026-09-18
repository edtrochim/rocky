---
id: registry:L31:BGr
kind: class
title: BGr Burnt grassland
system: registry:L31
code: BGr
name: Burnt grassland
status: registered
decomposed: true
file_class_id: '56'
n_rows: 53
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L31
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
- okf/registry/_raw/L31/L31.lccs
schema: okf/0.1
---

# BGr Burnt grassland

## Definition (verbatim, FAO LCLR)

Vegetation in extensive areas, herbaceous or shrub type of natural or planted origin where fires occurred. Fires can be man made or natural origin.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 57 | 58 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic; LC_BurntStatusCharacteristic |
| 57 | 60 Optional | `LC_Tree` | Mandatory | 0.0–10.0 |  | LC_VegetationArtificialityCharacteristic; LC_BurntStatusCharacteristic |
| 57 | 5C Optional | `LC_Shrub` | Mandatory | 0.0–20.0 |  | LC_VegetationArtificialityCharacteristic; LC_BurntStatusCharacteristic |

Full rows: `../elements.csv`, class_id `56`.
