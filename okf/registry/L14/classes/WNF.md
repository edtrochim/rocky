---
id: registry:L14:WNF
kind: class
title: WNF Waterbody natural
system: registry:L14
code: WNF
name: Waterbody natural
status: registered
decomposed: true
file_class_id: '41'
n_rows: 24
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L14
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L14/L14.lccs
schema: okf/0.1
---

# WNF Waterbody natural

## Definition (verbatim, FAO LCLR)

Natural fresh water lake

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 42 | 43 Mandatory | `LC_WaterBody` | Mandatory |  | position=Above Surface; dynamics=Standing | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `41`.
