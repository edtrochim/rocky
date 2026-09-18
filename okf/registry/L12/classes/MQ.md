---
id: registry:L12:MQ
kind: class
title: MQ Mines & quarries
system: registry:L12
code: MQ
name: Mines & quarries
status: registered
decomposed: true
file_class_id: '25'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_NonBuiltUpSurface
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_NonBuiltUpSurface
  path: ../../../vocab/elements/LC_NonBuiltUpSurface.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# MQ Mines & quarries

## Definition (verbatim, FAO LCLR)

Major mines and quarries as well as temporary building material extraction and dumping sites.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 26 | 27 Mandatory | `LC_NonBuiltUpSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `25`.
