---
id: registry:L4:MF
kind: class
title: MF Mangrove forest
system: registry:L4
code: MF
name: Mangrove forest
status: registered
decomposed: true
file_class_id: '21'
n_rows: 34
rows_in: ../elements.csv
element_refs:
- LC_Tree
- LC_WaterBody
links:
- rel: in_system
  id: registry:L4
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L4/L4.lccs
schema: okf/0.1
---

# MF Mangrove forest

## Definition (verbatim, FAO LCLR)

Saltwater mangrove forest

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 22 | 23 Mandatory | `LC_Tree` | Mandatory | 60.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 22 | 54 Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Brackish) |

Full rows: `../elements.csv`, class_id `21`.
