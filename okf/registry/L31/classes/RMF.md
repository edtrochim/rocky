---
id: registry:L31:RMF
kind: class
title: RMF Regenerating Miombo forest
system: registry:L31
code: RMF
name: Regenerating Miombo forest
status: registered
decomposed: true
file_class_id: '74'
n_rows: 30
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

# RMF Regenerating Miombo forest

## Definition (verbatim, FAO LCLR)

Miombo woodland or “panda forest” is a type of vegetation where trees predominate, belonging to the genera Brachystegia, Isoberlinia and Julbernardia. It is considered regenerating miombo with a vegetation composition of shrubs and other pioneers species. Depending on the regeneration rate, which in Angola is lower compared to other countries in the Miombo region, the land cover area in an area can be between 15 and 20%

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 75 | 76 Mandatory | `LC_Shrub` | Mandatory | 10.0–30.0 |  | LC_VegetationArtificialityCharacteristic |
| 75 | 79 Mandatory | `LC_Tree` | Mandatory | 10.0–30.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `74`.
