---
id: registry:L13:SCOa
kind: class
title: SCOa Closed to Open Shrubs (acquatic)
system: registry:L13
code: SCOa
name: Closed to Open Shrubs (acquatic)
status: registered
decomposed: true
file_class_id: '59'
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

# SCOa Closed to Open Shrubs (acquatic)

## Definition (verbatim, FAO LCLR)

Closed to open (15-100%) shrubs in flooded environments.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 5A | 5B Mandatory | `LC_Shrub` | Mandatory | 15.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 5A | 5E Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Brackish) |

Full rows: `../elements.csv`, class_id `59`.
