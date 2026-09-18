---
id: registry:L25:Ea
kind: class
title: Ea Artificial water bodies
system: registry:L25
code: Ea
name: Artificial water bodies
status: registered
decomposed: true
file_class_id: '352'
n_rows: 22
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

# Ea Artificial water bodies

## Definition (verbatim, FAO LCLR)

It corresponds to artificial water bodies which are permanent and/or seasonal feature in an area.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 353 | 354 Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Artificial); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `352`.
