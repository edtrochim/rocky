---
id: registry:L14:SA
kind: class
title: SA Salt evaporation ponds
system: registry:L14
code: SA
name: Salt evaporation ponds
status: registered
decomposed: true
file_class_id: 9F
n_rows: 33
rows_in: ../elements.csv
element_refs:
- LC_InorganicDeposits
- LC_WaterBody
links:
- rel: in_system
  id: registry:L14
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_InorganicDeposits
  path: ../../../vocab/elements/LC_InorganicDeposits.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L14/L14.lccs
schema: okf/0.1
---

# SA Salt evaporation ponds

## Definition (verbatim, FAO LCLR)

Artificial ponds to extract salt from sea water

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| A0 | A1 Mandatory | `LC_InorganicDeposits` | Mandatory |  | type=Salt Flat |  |
| A3 | A4 Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Saline) |

Full rows: `../elements.csv`, class_id `9F`.
