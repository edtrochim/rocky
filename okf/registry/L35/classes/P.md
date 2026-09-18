---
id: registry:L35:P
kind: class
title: P Port
system: registry:L35
code: P
name: Port
status: registered
decomposed: true
file_class_id: 10F
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_LinearSurface
links:
- rel: in_system
  id: registry:L35
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_LinearSurface
  path: ../../../vocab/elements/LC_LinearSurface.md
sources:
- okf/registry/_raw/L35/L35.lccs
schema: okf/0.1
---

# P Port

## Definition (verbatim, FAO LCLR)

NA

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 110 | 111 Mandatory | `LC_LinearSurface` | Mandatory |  |  | LC_ConstructionUse (type=Port Area) |

Full rows: `../elements.csv`, class_id `10F`.
