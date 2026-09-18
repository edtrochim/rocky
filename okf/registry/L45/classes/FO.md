---
id: registry:L45:FO
kind: class
title: FO Closed shrubs
system: registry:L45
code: FO
name: Closed shrubs
status: registered
decomposed: true
file_class_id: '16'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_Shrub
links:
- rel: in_system
  id: registry:L45
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L45/L45.lccs
schema: okf/0.1
---

# FO Closed shrubs

## Definition (verbatim, FAO LCLR)

Lands with woody vegetation between 2 and 5m tall and with shrub canopy cover >70%. Either evergreen or deciduous.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 17 | 18 Mandatory | `LC_Shrub` | Mandatory | 70.0–100.0 | height 2.0–5.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `16`.
