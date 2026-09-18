---
id: registry:L7:Se
kind: class
title: Se Sebkha
system: registry:L7
code: Se
name: Sebkha
status: registered
decomposed: true
file_class_id: DB
n_rows: 24
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L7
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L7/L7.lccs
schema: okf/0.1
---

# Se Sebkha

## Definition (verbatim, FAO LCLR)

Flat and very saline areas of sand or silt lying just above the water-table.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| DD | DE Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_WaterSalinityCharacteristic (type=Saline); LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `DB`.
