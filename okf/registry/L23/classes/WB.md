---
id: registry:L23:WB
kind: class
title: WB Water body
system: registry:L23
code: WB
name: Water body
status: registered
decomposed: true
file_class_id: 1F
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L23
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L23/L23.lccs
schema: okf/0.1
---

# WB Water body

## Definition (verbatim, FAO LCLR)

Perennial freshwater, natural or artificial

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 20 | 21 Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_WaterSalinityCharacteristic (type=Fresh); LC_ArtificialityCharacteristic (type=Artificial) |

Full rows: `../elements.csv`, class_id `1F`.
