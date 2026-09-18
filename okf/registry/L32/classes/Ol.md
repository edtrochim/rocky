---
id: registry:L32:Ol
kind: class
title: Ol Open land
system: registry:L32
code: Ol
name: Open land
status: registered
decomposed: true
file_class_id: '48'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
links:
- rel: in_system
  id: registry:L32
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
sources:
- okf/registry/_raw/L32/L32.lccs
schema: okf/0.1
---

# Ol Open land

## Definition (verbatim, FAO LCLR)

Natural bare surface areas.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 49 | 4A Mandatory | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `48`.
