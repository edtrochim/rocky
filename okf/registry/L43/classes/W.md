---
id: registry:L43:W
kind: class
title: W Water
system: registry:L43
code: W
name: Water
status: registered
decomposed: true
file_class_id: '2'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L43
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L43/L43.lccs
schema: okf/0.1
---

# W Water

## Definition (verbatim, FAO LCLR)

Area covered by natural or artificial water bodies.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3 | 4 Mandatory | `LC_WaterBody` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `2`.
