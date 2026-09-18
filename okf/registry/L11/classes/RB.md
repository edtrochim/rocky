---
id: registry:L11:RB
kind: class
title: RB River bank
system: registry:L11
code: RB
name: River bank
status: registered
decomposed: true
file_class_id: 11D
n_rows: 35
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L11
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L11/L11.lccs
schema: okf/0.1
---

# RB River bank

## Definition (verbatim, FAO LCLR)

River bank (soil/sand deposits) + perennial / periodic flowing fresh water.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 11E | 121 Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_WaterSalinityCharacteristic (type=Fresh) |
| 11E | 124 Optional | `LC_HerbaceousGrowthForm` | Mandatory | 0.0–10.0 |  |  |
| 11E | 11F Mandatory | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `11D`.
