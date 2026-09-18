---
id: registry:L8:R
kind: class
title: R Rivers/khals
system: registry:L8
code: R
name: Rivers/khals
status: registered
decomposed: true
file_class_id: F0
n_rows: 20
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L8
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L8/L8.lccs
schema: okf/0.1
---

# R Rivers/khals

## Definition (verbatim, FAO LCLR)

Natural water courses serving as water drainage channels.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| F1 | F2 Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Flowing; position=Above Surface | LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `F0`.
