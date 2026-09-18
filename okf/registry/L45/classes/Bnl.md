---
id: registry:L45:Bnl
kind: class
title: Bnl Built-up non linear
system: registry:L45
code: Bnl
name: Built-up non linear
status: registered
decomposed: true
file_class_id: '91'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_NonLinearSurface
links:
- rel: in_system
  id: registry:L45
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_NonLinearSurface
  path: ../../../vocab/elements/LC_NonLinearSurface.md
sources:
- okf/registry/_raw/L45/L45.lccs
schema: okf/0.1
---

# Bnl Built-up non linear

## Definition (verbatim, FAO LCLR)

Land covered by buildings and other man-made structures.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 92 | 93 Mandatory | `LC_NonLinearSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `91`.
