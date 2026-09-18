---
id: registry:L23:BRS
kind: class
title: BRS Bare soil
system: registry:L23
code: BRS
name: Bare soil
status: registered
decomposed: true
file_class_id: '16'
n_rows: 16
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
links:
- rel: in_system
  id: registry:L23
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
sources:
- okf/registry/_raw/L23/L23.lccs
schema: okf/0.1
---

# BRS Bare soil

## Definition (verbatim, FAO LCLR)

Unconsolidated bare soil.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 18 | 19 Mandatory | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `16`.
