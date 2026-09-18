---
id: registry:L14:UA
kind: class
title: UA Urban areas
system: registry:L14
code: UA
name: Urban areas
status: registered
decomposed: true
file_class_id: E
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_Building
links:
- rel: in_system
  id: registry:L14
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
sources:
- okf/registry/_raw/L14/L14.lccs
schema: okf/0.1
---

# UA Urban areas

## Definition (verbatim, FAO LCLR)

Urban build-up areas

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| F | 10 Mandatory | `LC_Building` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `E`.
