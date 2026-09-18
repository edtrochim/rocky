---
id: registry:L30:Sbc
kind: class
title: Sbc Continental sebkha
system: registry:L30
code: Sbc
name: Continental sebkha
status: registered
decomposed: true
file_class_id: 17A
n_rows: 34
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_InorganicDeposits
- LC_WaterBody
links:
- rel: in_system
  id: registry:L30
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_InorganicDeposits
  path: ../../../vocab/elements/LC_InorganicDeposits.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L30/L30.lccs
schema: okf/0.1
---

# Sbc Continental sebkha

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 17B | 17C Mandatory | `LC_BareSoil` | Mandatory |  |  |  |
| 17B | 17C Mandatory | `LC_InorganicDeposits` | Optional |  |  |  |
| 17B | 17F Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Brackish) |

Full rows: `../elements.csv`, class_id `17A`.
