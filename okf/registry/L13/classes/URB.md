---
id: registry:L13:URB
kind: class
title: URB Urban Area(s)
system: registry:L13
code: URB
name: Urban Area(s)
status: registered
decomposed: true
file_class_id: 6B
n_rows: 17
rows_in: ../elements.csv
element_refs:
- LC_BuiltUpSurface
links:
- rel: in_system
  id: registry:L13
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BuiltUpSurface
  path: ../../../vocab/elements/LC_BuiltUpSurface.md
sources:
- okf/registry/_raw/L13/L13.lccs
schema: okf/0.1
---

# URB Urban Area(s)

## Definition (verbatim, FAO LCLR)

Refers to any artificial surfaces (urban, industrial, eTc.)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 6D | 6E Mandatory | `LC_BuiltUpSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `6B`.
