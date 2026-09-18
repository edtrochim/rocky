---
id: registry:L13:BS
kind: class
title: BS Bare Rocks and Soil and/or Other Unconsolidated Material(s)
system: registry:L13
code: BS
name: Bare Rocks and Soil and/or Other Unconsolidated Material(s)
status: registered
decomposed: true
file_class_id: '70'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
links:
- rel: in_system
  id: registry:L13
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
sources:
- okf/registry/_raw/L13/L13.lccs
schema: okf/0.1
---

# BS Bare Rocks and Soil and/or Other Unconsolidated Material(s)

## Definition (verbatim, FAO LCLR)

This class consists of bare areas including quarries.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 71 | 72 Mandatory | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `70`.
