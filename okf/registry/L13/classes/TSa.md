---
id: registry:L13:TSa
kind: class
title: TSa Sparse Trees.(acquatic)
system: registry:L13
code: TSa
name: Sparse Trees.(acquatic)
status: registered
decomposed: true
file_class_id: '35'
n_rows: 34
rows_in: ../elements.csv
element_refs:
- LC_Tree
- LC_WaterBody
links:
- rel: in_system
  id: registry:L13
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L13/L13.lccs
schema: okf/0.1
---

# TSa Sparse Trees.(acquatic)

## Definition (verbatim, FAO LCLR)

Sparse (<15%) trees in flooded environments.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 36 | 37 Mandatory | `LC_Tree` | Mandatory | 1.0–15.0 |  | LC_VegetationArtificialityCharacteristic |
| 36 | 3A Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Brackish) |

Full rows: `../elements.csv`, class_id `35`.
