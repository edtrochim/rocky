---
id: registry:L32:R
kind: class
title: R River/stream
system: registry:L32
code: R
name: River/stream
status: registered
decomposed: true
file_class_id: 3D
n_rows: 23
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L32
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L32/L32.lccs
schema: okf/0.1
---

# R River/stream

## Definition (verbatim, FAO LCLR)

Permanent water body surrounded by land with fresh water.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3E | 3F Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Flowing | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `3D`.
