---
id: registry:L13:HSa
kind: class
title: HSa Sparse Herbaceous Vegetation (acquatic)
system: registry:L13
code: HSa
name: Sparse Herbaceous Vegetation (acquatic)
status: registered
decomposed: true
file_class_id: '47'
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

# HSa Sparse Herbaceous Vegetation (acquatic)

## Definition (verbatim, FAO LCLR)

Sparse (<15%) herbaceous in flooded environments.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 48 | 49 Mandatory | `LC_Shrub` | Mandatory | 1.0–15.0 |  | LC_VegetationArtificialityCharacteristic |
| 48 | 4C Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Brackish) |

Full rows: `../elements.csv`, class_id `47`.
