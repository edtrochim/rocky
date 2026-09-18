---
id: registry:L7:D
kind: class
title: D Dams
system: registry:L7
code: D
name: Dams
status: registered
decomposed: true
file_class_id: E2
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L7
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L7/L7.lccs
schema: okf/0.1
---

# D Dams

## Definition (verbatim, FAO LCLR)

Water body result of a barrier that stops or restricts the flow of surface water or underground streams.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| E3 | E4 Mandatory | `LC_WaterBody` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `E2`.
