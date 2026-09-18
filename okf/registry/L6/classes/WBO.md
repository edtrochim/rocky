---
id: registry:L6:WBO
kind: class
title: WBO Water bodies
system: registry:L6
code: WBO
name: Water bodies
status: registered
decomposed: true
file_class_id: '52'
n_rows: 15
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L6
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L6/L6.lccs
schema: okf/0.1
---

# WBO Water bodies

## Definition (verbatim, FAO LCLR)

Natural and artificial non-perennial fresh water body (flowing and stand-ing).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 53 | 54 Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Flowing and standing |  |

Full rows: `../elements.csv`, class_id `52`.
