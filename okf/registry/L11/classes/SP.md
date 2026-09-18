---
id: registry:L11:SP
kind: class
title: SP Saltpans
system: registry:L11
code: SP
name: Saltpans
status: registered
decomposed: true
file_class_id: 9F
n_rows: 31
rows_in: ../elements.csv
element_refs:
- LC_InorganicDeposits
- LC_WaterBody
links:
- rel: in_system
  id: registry:L11
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_InorganicDeposits
  path: ../../../vocab/elements/LC_InorganicDeposits.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L11/L11.lccs
schema: okf/0.1
---

# SP Saltpans

## Definition (verbatim, FAO LCLR)

Artificial ponds to extract salt from saline water body.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| A0 | 155 Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Artificial); LC_WaterSalinityCharacteristic (type=Saline) |
| A0 | A1 Mandatory | `LC_InorganicDeposits` | Mandatory |  | type=Salt Flat |  |

Full rows: `../elements.csv`, class_id `9F`.
