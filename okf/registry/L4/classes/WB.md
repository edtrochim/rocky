---
id: registry:L4:WB
kind: class
title: WB Water bodies
system: registry:L4
code: WB
name: Water bodies
status: registered
decomposed: true
file_class_id: 4B
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L4
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L4/L4.lccs
schema: okf/0.1
---

# WB Water bodies

## Definition (verbatim, FAO LCLR)

Water bodies.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4C | 4D Mandatory | `LC_WaterBody` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `4B`.
