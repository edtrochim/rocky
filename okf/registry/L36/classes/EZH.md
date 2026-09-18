---
id: registry:L36:EZH
kind: class
title: EZH Water and wetlands
system: registry:L36
code: EZH
name: Water and wetlands
status: registered
decomposed: true
file_class_id: '134'
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L36
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L36/L36.lccs
schema: okf/0.1
---

# EZH Water and wetlands

## Definition (verbatim, FAO LCLR)

The land is covered by water areas. Within this land cover class are included natural and artificial non - perennial freshwater body (flowing and standing).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 135 | 136 Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `134`.
