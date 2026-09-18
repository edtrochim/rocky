---
id: registry:L11:SS
kind: class
title: SS Saline soil/halophytes
system: registry:L11
code: SS
name: Saline soil/halophytes
status: registered
decomposed: true
file_class_id: '163'
n_rows: 23
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_InorganicDeposits
links:
- rel: in_system
  id: registry:L11
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_InorganicDeposits
  path: ../../../vocab/elements/LC_InorganicDeposits.md
sources:
- okf/registry/_raw/L11/L11.lccs
schema: okf/0.1
---

# SS Saline soil/halophytes

## Definition (verbatim, FAO LCLR)

Flat expanse of ground covered with salty soil and sparse vegetation outcrops.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 164 | 165 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 0.0–20.0 |  | LC_VegetationArtificialityCharacteristic |
| 164 | 165 Mandatory | `LC_InorganicDeposits` | Mandatory |  | type=Salt Flat |  |

Full rows: `../elements.csv`, class_id `163`.
