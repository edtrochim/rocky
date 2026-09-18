---
id: registry:L14:WNS
kind: class
title: WNS Waterbody natural saline
system: registry:L14
code: WNS
name: Waterbody natural saline
status: registered
decomposed: true
file_class_id: '18'
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

# WNS Waterbody natural saline

## Definition (verbatim, FAO LCLR)

Saline water lake (Dead Sea)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 19 | 1A Mandatory | `LC_WaterBody` | Mandatory |  | position=Above Surface; dynamics=Standing | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Saline) |

Full rows: `../elements.csv`, class_id `18`.
