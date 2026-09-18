---
id: registry:L3:FC
kind: class
title: FC Forest Closed
system: registry:L3
code: FC
name: Forest Closed
status: registered
decomposed: true
file_class_id: '71'
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L3
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L3/L3.lccs
schema: okf/0.1
---

# FC Forest Closed

## Definition (verbatim, FAO LCLR)

Woodland with closed (60-100%) trees and/or shrubs

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 72 | 73 Mandatory | `LC_WoodyGrowthForm` | Mandatory | 60.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `71`.
