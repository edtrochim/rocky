---
id: registry:L29:lcc3
kind: class
title: lcc3 Built-up
system: registry:L29
code: lcc3
name: Built-up
status: registered
decomposed: true
file_class_id: 2E
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_LinearSurface
- LC_NonLinearSurface
links:
- rel: in_system
  id: registry:L29
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_LinearSurface
  path: ../../../vocab/elements/LC_LinearSurface.md
- rel: uses_type
  id: element:LC_NonLinearSurface
  path: ../../../vocab/elements/LC_NonLinearSurface.md
sources:
- okf/registry/_raw/L29/L29.lccs
schema: okf/0.1
---

# lcc3 Built-up

## Definition (verbatim, FAO LCLR)

Built-up areas refer to artificial structures such as towns, villages, industrial areas, airports, etc.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2F | 30 Mandatory | `LC_LinearSurface` | Mandatory |  |  |  |
| 2F | 30 Mandatory | `LC_NonLinearSurface` | Optional |  |  |  |

Full rows: `../elements.csv`, class_id `2E`.
