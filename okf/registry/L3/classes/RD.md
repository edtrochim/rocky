---
id: registry:L3:RD
kind: class
title: RD Roads
system: registry:L3
code: RD
name: Roads
status: registered
decomposed: true
file_class_id: 16B
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_LinearSurface
links:
- rel: in_system
  id: registry:L3
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_LinearSurface
  path: ../../../vocab/elements/LC_LinearSurface.md
sources:
- okf/registry/_raw/L3/L3.lccs
schema: okf/0.1
---

# RD Roads

## Definition (verbatim, FAO LCLR)

Roads

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 16C | 16D Mandatory | `LC_LinearSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `16B`.
