---
id: registry:L13:SSa
kind: class
title: SSa Sparse Shrubs (acquatic)
system: registry:L13
code: SSa
name: Sparse Shrubs (acquatic)
status: registered
decomposed: true
file_class_id: 3E
n_rows: 34
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_WaterBody
links:
- rel: in_system
  id: registry:L13
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L13/L13.lccs
schema: okf/0.1
---

# SSa Sparse Shrubs (acquatic)

## Definition (verbatim, FAO LCLR)

Sparse (<15%) shrubs in flooded environments.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3F | 40 Mandatory | `LC_Shrub` | Mandatory | 1.0–15.0 |  | LC_VegetationArtificialityCharacteristic |
| 3F | 43 Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Brackish) |

Full rows: `../elements.csv`, class_id `3E`.
