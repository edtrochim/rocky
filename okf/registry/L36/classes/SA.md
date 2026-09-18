---
id: registry:L36:SA
kind: class
title: SA Infrastructure
system: registry:L36
code: SA
name: Infrastructure
status: registered
decomposed: true
file_class_id: 14F
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_BuiltUpSurface
- LC_NonBuiltUpSurface
links:
- rel: in_system
  id: registry:L36
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BuiltUpSurface
  path: ../../../vocab/elements/LC_BuiltUpSurface.md
- rel: uses_type
  id: element:LC_NonBuiltUpSurface
  path: ../../../vocab/elements/LC_NonBuiltUpSurface.md
sources:
- okf/registry/_raw/L36/L36.lccs
schema: okf/0.1
---

# SA Infrastructure

## Definition (verbatim, FAO LCLR)

The land is covered by infrastructure as buildings, roads and artifiical surfaced areas. Different types of buildup are included in this class (i.e. urban, airports, oilfields).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 150 | 151 Mandatory | `LC_BuiltUpSurface` | Mandatory |  |  |  |
| 150 | 207 Optional | `LC_NonBuiltUpSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `14F`.
