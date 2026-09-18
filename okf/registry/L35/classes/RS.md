---
id: registry:L35:RS
kind: class
title: RS Rural settlement
system: registry:L35
code: RS
name: Rural settlement
status: registered
decomposed: true
file_class_id: '118'
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_BuiltUpSurface
links:
- rel: in_system
  id: registry:L35
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BuiltUpSurface
  path: ../../../vocab/elements/LC_BuiltUpSurface.md
sources:
- okf/registry/_raw/L35/L35.lccs
schema: okf/0.1
---

# RS Rural settlement

## Definition (verbatim, FAO LCLR)

NA

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 119 | 11A Mandatory | `LC_BuiltUpSurface` | Mandatory |  |  | LC_ConstructionUse (type=Rural) |

Full rows: `../elements.csv`, class_id `118`.
