---
id: registry:L20:Ur
kind: class
title: Ur Urban area
system: registry:L20
code: Ur
name: Urban area
status: registered
decomposed: true
file_class_id: A5
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_Building
- LC_LinearSurface
- LC_Tree
links:
- rel: in_system
  id: registry:L20
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
- rel: uses_type
  id: element:LC_LinearSurface
  path: ../../../vocab/elements/LC_LinearSurface.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L20/L20.lccs
schema: okf/0.1
---

# Ur Urban area

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| A6 | 123 Mandatory | `LC_Tree` | Mandatory | 0.0–20.0 | height 0.0–30.0 |  |
| A6 | A7 Mandatory | `LC_Building` | Mandatory | 30.0–100.0 |  |  |
| A6 | A7 Mandatory | `LC_LinearSurface` | Optional | 0.0–30.0 |  |  |

Full rows: `../elements.csv`, class_id `A5`.
