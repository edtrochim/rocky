---
id: registry:L25:R
kind: class
title: R River
system: registry:L25
code: R
name: River
status: registered
decomposed: true
file_class_id: 32E
n_rows: 23
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# R River

## Definition (verbatim, FAO LCLR)

The rivers are natural water courses which serves as water drainage channels

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 32F | 330 Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Flowing | LC_WaterSalinityCharacteristic (type=Fresh); LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `32E`.
