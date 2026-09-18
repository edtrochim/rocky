---
id: registry:L31:Gra
kind: class
title: Gra Grassland
system: registry:L31
code: Gra
name: Grassland
status: registered
decomposed: true
file_class_id: 4A
n_rows: 45
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

# Gra Grassland

## Definition (verbatim, FAO LCLR)

Vegetation in extensive areas, herbaceous or shrub type of natural or planted origin, with scattered trees.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4B | 50 Optional | `LC_Shrub` | Mandatory | 0.0–20.0 |  | LC_VegetationArtificialityCharacteristic |
| 4B | 53 Optional | `LC_Tree` | Mandatory | 0.0–10.0 |  | LC_VegetationArtificialityCharacteristic |
| 4B | 4C Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 70.0–100.0 |  | LC_VegetationArtificialityCharacteristic; LC_GrazedCharacteristic |

Full rows: `../elements.csv`, class_id `4A`.
