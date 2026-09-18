---
id: registry:L48:Wb
kind: class
title: Wb Water body
system: registry:L48
code: Wb
name: Water body
status: registered
decomposed: true
file_class_id: '25'
n_rows: 15
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L48
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L48/L48.lccs
schema: okf/0.1
---

# Wb Water body

## Definition (verbatim, FAO LCLR)

Water bodies that include both natural and artificial waterbodies. The class includes rivers, ponds, and lakes.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 26 | 27 Mandatory | `LC_WaterBody` | Mandatory |  | position=Above Surface |  |

Full rows: `../elements.csv`, class_id `25`.
