---
id: registry:L23:WDL
kind: class
title: WDL Woodland
system: registry:L23
code: WDL
name: Woodland
status: registered
decomposed: true
file_class_id: '2'
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L23
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L23/L23.lccs
schema: okf/0.1
---

# WDL Woodland

## Definition (verbatim, FAO LCLR)

Natural land covered with trees or shrubs (> 10 % canopy cover)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3 | 4 Mandatory | `LC_Tree` | Mandatory | 10.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 3 | 7 Mandatory | `LC_Shrub` | Mandatory | 10.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `2`.
