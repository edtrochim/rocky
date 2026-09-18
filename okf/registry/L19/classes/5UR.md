---
id: registry:L19:5UR
kind: class
title: 5UR Urban areas
system: registry:L19
code: 5UR
name: Urban areas
status: registered
decomposed: true
file_class_id: '3'
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_BuiltUpSurface
links:
- rel: in_system
  id: registry:L19
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BuiltUpSurface
  path: ../../../vocab/elements/LC_BuiltUpSurface.md
sources:
- okf/registry/_raw/L19/L19.lccs
schema: okf/0.1
---

# 5UR Urban areas

## Definition (verbatim, FAO LCLR)

Urban area(s)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4 | 5 Mandatory | `LC_BuiltUpSurface` | Mandatory |  |  | LC_ConstructionUse (type=Residential) |

Full rows: `../elements.csv`, class_id `3`.
