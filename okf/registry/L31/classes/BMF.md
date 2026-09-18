---
id: registry:L31:BMF
kind: class
title: BMF Burnt Miombo forest
system: registry:L31
code: BMF
name: Burnt Miombo forest
status: registered
decomposed: true
file_class_id: 7D
n_rows: 38
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L31
  path: ../SYSTEM.md
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

# BMF Burnt Miombo forest

## Definition (verbatim, FAO LCLR)

Miombo woodland or “panda forest” is a type of vegetation where trees predominate, belonging to the genera Brachystegia, Isoberlinia and Julbernardia. No green woodland vegetation is present on the land.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 7E | 83 Mandatory | `LC_Tree` | Mandatory | 10.0–30.0 |  | LC_VegetationArtificialityCharacteristic; LC_BurntStatusCharacteristic |
| 7E | 7F Mandatory | `LC_Shrub` | Mandatory | 10.0–30.0 |  | LC_VegetationArtificialityCharacteristic; LC_BurntStatusCharacteristic |

Full rows: `../elements.csv`, class_id `7D`.
