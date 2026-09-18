---
id: registry:L32:Bl
kind: class
title: Bl Built-up linear
system: registry:L32
code: Bl
name: Built-up linear
status: registered
decomposed: true
file_class_id: '50'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_LinearSurface
links:
- rel: in_system
  id: registry:L32
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_LinearSurface
  path: ../../../vocab/elements/LC_LinearSurface.md
sources:
- okf/registry/_raw/L32/L32.lccs
schema: okf/0.1
---

# Bl Built-up linear

## Definition (verbatim, FAO LCLR)

Land area corresponds to artificial surface which are built-up linear.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 51 | 52 Mandatory | `LC_LinearSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `50`.
