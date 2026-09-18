---
id: registry:L8:Ap
kind: class
title: Ap Air port
system: registry:L8
code: Ap
name: Air port
status: registered
decomposed: true
file_class_id: 35D
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_BuiltUpSurface
links:
- rel: in_system
  id: registry:L8
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BuiltUpSurface
  path: ../../../vocab/elements/LC_BuiltUpSurface.md
sources:
- okf/registry/_raw/L8/L8.lccs
schema: okf/0.1
---

# Ap Air port

## Definition (verbatim, FAO LCLR)

Built-up areas with facilities for flights to take off and land.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 35E | 35F Mandatory | `LC_BuiltUpSurface` | Mandatory |  |  | LC_ConstructionUse (type=Airport) |

Full rows: `../elements.csv`, class_id `35D`.
