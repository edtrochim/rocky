---
id: registry:L38:BU
kind: class
title: BU Built-up area
system: registry:L38
code: BU
name: Built-up area
status: registered
decomposed: true
file_class_id: F2
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_Building
links:
- rel: in_system
  id: registry:L38
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
sources:
- okf/registry/_raw/L38/L38.lccs
schema: okf/0.1
---

# BU Built-up area

## Definition (verbatim, FAO LCLR)

High and medium density urban built-up area occasionally with trees. Different types of costruction are included

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| F3 | F4 Mandatory | `LC_Building` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `F2`.
