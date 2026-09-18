---
id: registry:L45:Bla
kind: class
title: Bla Built-up linear and barren
system: registry:L45
code: Bla
name: Built-up linear and barren
status: registered
decomposed: true
file_class_id: '95'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_LinearSurface
links:
- rel: in_system
  id: registry:L45
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_LinearSurface
  path: ../../../vocab/elements/LC_LinearSurface.md
sources:
- okf/registry/_raw/L45/L45.lccs
schema: okf/0.1
---

# Bla Built-up linear and barren

## Definition (verbatim, FAO LCLR)

Artificial surface where linear elements / Lands with exposed soil, sand, rocks, or snow and never have more than 10% vegetated.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 96 | 97 Mandatory | `LC_LinearSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `95`.
