---
id: registry:L2:8WF
kind: class
title: 8WF Rivers
system: registry:L2
code: 8WF
name: Rivers
status: registered
decomposed: true
file_class_id: '106'
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

# 8WF Rivers

## Definition (verbatim, FAO LCLR)

Rivers

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 107 | 108 Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Flowing |  |

Full rows: `../elements.csv`, class_id `106`.
