---
id: registry:L32:Bnl
kind: class
title: Bnl Built-up non-linear
system: registry:L32
code: Bnl
name: Built-up non-linear
status: registered
decomposed: true
file_class_id: 4C
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_NonLinearSurface
links:
- rel: in_system
  id: registry:L32
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_NonLinearSurface
  path: ../../../vocab/elements/LC_NonLinearSurface.md
sources:
- okf/registry/_raw/L32/L32.lccs
schema: okf/0.1
---

# Bnl Built-up non-linear

## Definition (verbatim, FAO LCLR)

Land area corresponds to artificial surface which are built-up non-linear.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4D | 4E Mandatory | `LC_NonLinearSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `4C`.
