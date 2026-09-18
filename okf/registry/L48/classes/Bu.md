---
id: registry:L48:Bu
kind: class
title: Bu Built-up
system: registry:L48
code: Bu
name: Built-up
status: registered
decomposed: true
file_class_id: '21'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_BuiltUpSurface
links:
- rel: in_system
  id: registry:L48
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BuiltUpSurface
  path: ../../../vocab/elements/LC_BuiltUpSurface.md
sources:
- okf/registry/_raw/L48/L48.lccs
schema: okf/0.1
---

# Bu Built-up

## Definition (verbatim, FAO LCLR)

This class includes artificial surfaces, both non-linear and linear built-up areas including roadways, industrial area, port, airport, urban area, rural settlements, and refugee camp.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 22 | 23 Mandatory | `LC_BuiltUpSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `21`.
