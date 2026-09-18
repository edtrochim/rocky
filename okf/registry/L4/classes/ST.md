---
id: registry:L4:ST
kind: class
title: ST Settlements
system: registry:L4
code: ST
name: Settlements
status: registered
decomposed: true
file_class_id: '47'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_Building
links:
- rel: in_system
  id: registry:L4
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
sources:
- okf/registry/_raw/L4/L4.lccs
schema: okf/0.1
---

# ST Settlements

## Definition (verbatim, FAO LCLR)

Built-up areas.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 48 | 49 Mandatory | `LC_Building` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `47`.
