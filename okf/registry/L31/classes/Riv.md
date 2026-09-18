---
id: registry:L31:Riv
kind: class
title: Riv River
system: registry:L31
code: Riv
name: River
status: registered
decomposed: true
file_class_id: '87'
n_rows: 23
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L31
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L31/L31.lccs
schema: okf/0.1
---

# Riv River

## Definition (verbatim, FAO LCLR)

Natural water course that flows into another, into the sea or into a lake.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 88 | 89 Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Flowing | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `87`.
