---
id: registry:L38:WBP
kind: class
title: WBP Water body perennial/artificial pond
system: registry:L38
code: WBP
name: Water body perennial/artificial pond
status: registered
decomposed: true
file_class_id: '220'
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L38
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L38/L38.lccs
schema: okf/0.1
---

# WBP Water body perennial/artificial pond

## Definition (verbatim, FAO LCLR)

Natural perennial fresh waterbody and artificial waterbody

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 221 | 222 Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Artificial); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `220`.
