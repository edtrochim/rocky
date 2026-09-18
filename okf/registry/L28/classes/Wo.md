---
id: registry:L28:Wo
kind: class
title: Wo Water ocean
system: registry:L28
code: Wo
name: Water ocean
status: registered
decomposed: true
file_class_id: 9A
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L28
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L28/L28.lccs
schema: okf/0.1
---

# Wo Water ocean

## Definition (verbatim, FAO LCLR)

Water bodies include oceans.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 9B | 9C Mandatory | `LC_WaterBody` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `9A`.
