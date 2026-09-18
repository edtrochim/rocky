---
id: registry:L12:BA
kind: class
title: BA Bare area
system: registry:L12
code: BA
name: Bare area
status: registered
decomposed: true
file_class_id: '47'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# BA Bare area

## Definition (verbatim, FAO LCLR)

Undifferentiated areas not used for cutivation and usually devoid of grass or shrub cover, commonly associated with degraded land and erosion effects, sometimes within or adjacent to urban and rural areas.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 48 | 49 Mandatory | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `47`.
