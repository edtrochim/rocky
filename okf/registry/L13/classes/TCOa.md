---
id: registry:L13:TCOa
kind: class
title: TCOa Closed to Open Trees (acquatic)
system: registry:L13
code: TCOa
name: Closed to Open Trees (acquatic)
status: registered
decomposed: true
file_class_id: '50'
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

# TCOa Closed to Open Trees (acquatic)

## Definition (verbatim, FAO LCLR)

Closed to open (15-100%) trees in flooded environments.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 51 | 52 Mandatory | `LC_Tree` | Mandatory | 15.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 51 | 55 Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Brackish) |

Full rows: `../elements.csv`, class_id `50`.
