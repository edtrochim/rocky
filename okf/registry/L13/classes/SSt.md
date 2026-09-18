---
id: registry:L13:SSt
kind: class
title: SSt Sparse Shrubs (terrestrial)
system: registry:L13
code: SSt
name: Sparse Shrubs (terrestrial)
status: registered
decomposed: true
file_class_id: '13'
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_Shrub
links:
- rel: in_system
  id: registry:L13
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L13/L13.lccs
schema: okf/0.1
---

# SSt Sparse Shrubs (terrestrial)

## Definition (verbatim, FAO LCLR)

Sparse shrub vegetation in terrestrial environment and coverage percentage is lower than 15%.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 14 | 15 Mandatory | `LC_Shrub` | Mandatory | 1.0–15.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `13`.
