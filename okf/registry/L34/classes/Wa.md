---
id: registry:L34:Wa
kind: class
title: Wa Water
system: registry:L34
code: Wa
name: Water
status: registered
decomposed: true
file_class_id: '37'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L34
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L34/L34.lccs
schema: okf/0.1
---

# Wa Water

## Definition (verbatim, FAO LCLR)

This land is characterized by the presence of water bodies, including both natural and artificial non - perennial freshwater bodies (flowing and stagnant).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 38 | 39 Mandatory | `LC_WaterBody` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `37`.
