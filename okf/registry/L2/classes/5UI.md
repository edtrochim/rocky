---
id: registry:L2:5UI
kind: class
title: 5UI Urban and industrial areas
system: registry:L2
code: 5UI
name: Urban and industrial areas
status: registered
decomposed: true
file_class_id: CB
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_NonLinearSurface
links:
- rel: in_system
  id: registry:L2
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_NonLinearSurface
  path: ../../../vocab/elements/LC_NonLinearSurface.md
sources:
- okf/registry/_raw/L2/L2.lccs
schema: okf/0.1
---

# 5UI Urban and industrial areas

## Definition (verbatim, FAO LCLR)

Urban and industrial areas

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| CC | CD Mandatory | `LC_NonLinearSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `CB`.
