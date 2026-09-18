---
id: registry:L11:BLR
kind: class
title: BLR Linear built-up
system: registry:L11
code: BLR
name: Linear built-up
status: registered
decomposed: true
file_class_id: 12E
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_LinearSurface
links:
- rel: in_system
  id: registry:L11
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_LinearSurface
  path: ../../../vocab/elements/LC_LinearSurface.md
sources:
- okf/registry/_raw/L11/L11.lccs
schema: okf/0.1
---

# BLR Linear built-up

## Definition (verbatim, FAO LCLR)

Major roads and railways.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 12F | 130 Mandatory | `LC_LinearSurface` | Mandatory |  |  |  |
| 12F | 130 Mandatory | `LC_LinearSurface` | Optional |  |  |  |

Full rows: `../elements.csv`, class_id `12E`.
