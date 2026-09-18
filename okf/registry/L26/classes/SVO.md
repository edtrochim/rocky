---
id: registry:L26:SVO
kind: class
title: SVO Shrubs very open
system: registry:L26
code: SVO
name: Shrubs very open
status: registered
decomposed: true
file_class_id: 2C
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

# SVO Shrubs very open

## Definition (verbatim, FAO LCLR)

Natural shrubs with cover (16-40%). Optional trees (0-15%) and herbs (0-50%).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 51 | 52 Mandatory | `LC_Shrub` | Mandatory | 16.0–40.0 |  | LC_VegetationArtificialityCharacteristic |
| 51 | 55 Optional | `LC_Tree` | Mandatory | 0.0–15.0 |  | LC_VegetationArtificialityCharacteristic |
| 51 | AC Optional | `LC_HerbaceousGrowthForm` | Mandatory | 0.0–50.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `2C`.
