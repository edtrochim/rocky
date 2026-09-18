---
id: registry:L13:HCOa
kind: class
title: HCOa Closed to Open Herbaceous Vegetation.
system: registry:L13
code: HCOa
name: Closed to Open Herbaceous Vegetation.
status: registered
decomposed: true
file_class_id: '62'
n_rows: 34
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L13
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L13/L13.lccs
schema: okf/0.1
---

# HCOa Closed to Open Herbaceous Vegetation.

## Definition (verbatim, FAO LCLR)

Closed to open (15-100%) herbaceous in flooded environments.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 63 | 64 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 15.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 63 | 67 Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Brackish) |

Full rows: `../elements.csv`, class_id `62`.
