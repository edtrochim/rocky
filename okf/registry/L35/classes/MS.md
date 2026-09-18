---
id: registry:L35:MS
kind: class
title: MS Closed to open mangrove shrubs
system: registry:L35
code: MS
name: Closed to open mangrove shrubs
status: registered
decomposed: true
file_class_id: 18D
n_rows: 35
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_WaterBody
links:
- rel: in_system
  id: registry:L35
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L35/L35.lccs
schema: okf/0.1
---

# MS Closed to open mangrove shrubs

## Definition (verbatim, FAO LCLR)

NA

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 18E | 191 Mandatory | `LC_WaterBody` | Mandatory |  | position=Above Surface; dynamics=Standing | LC_WaterSalinityCharacteristic (type=Brackish); LC_ArtificialityCharacteristic (type=Natural) |
| 18E | 18F Mandatory | `LC_Shrub` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `18D`.
