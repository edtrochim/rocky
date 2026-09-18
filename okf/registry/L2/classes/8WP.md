---
id: registry:L2:8WP
kind: class
title: 8WP Lakes
system: registry:L2
code: 8WP
name: Lakes
status: registered
decomposed: true
file_class_id: '102'
n_rows: 15
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L2
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L2/L2.lccs
schema: okf/0.1
---

# 8WP Lakes

## Definition (verbatim, FAO LCLR)

Lakes

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 103 | 104 Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Standing |  |

Full rows: `../elements.csv`, class_id `102`.
