---
id: registry:L45:R
kind: class
title: R Rivers
system: registry:L45
code: R
name: Rivers
status: registered
decomposed: true
file_class_id: '99'
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L45
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L45/L45.lccs
schema: okf/0.1
---

# R Rivers

## Definition (verbatim, FAO LCLR)

Flowing fresh water whose persistence is more than 9 months per year.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 9A | 9B Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_WaterSalinityCharacteristic (type=Fresh); LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `99`.
