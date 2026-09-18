---
id: registry:L38:RP
kind: class
title: RP River perennial
system: registry:L38
code: RP
name: River perennial
status: registered
decomposed: true
file_class_id: '69'
n_rows: 24
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L38
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L38/L38.lccs
schema: okf/0.1
---

# RP River perennial

## Definition (verbatim, FAO LCLR)

Water course

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 6A | 6B Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Flowing; position=Above Surface | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `69`.
