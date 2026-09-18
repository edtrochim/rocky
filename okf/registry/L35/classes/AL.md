---
id: registry:L35:AL
kind: class
title: AL Artificial lake
system: registry:L35
code: AL
name: Artificial lake
status: registered
decomposed: true
file_class_id: '135'
n_rows: 23
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L35
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L35/L35.lccs
schema: okf/0.1
---

# AL Artificial lake

## Definition (verbatim, FAO LCLR)

NA

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 136 | 137 Mandatory | `LC_WaterBody` | Mandatory |  | position=Above Surface | LC_ArtificialityCharacteristic (type=Artificial); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `135`.
