---
id: registry:L42:Bl
kind: class
title: Bl Bare land
system: registry:L42
code: Bl
name: Bare land
status: registered
decomposed: true
file_class_id: 4E
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
links:
- rel: in_system
  id: registry:L42
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
sources:
- okf/registry/_raw/L42/L42.lccs
schema: okf/0.1
---

# Bl Bare land

## Definition (verbatim, FAO LCLR)

Bare land without or with scattered vegetation consists of arid lands. This category is divided into bare rock, bare soil, beaches, sand dunes, and islands.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4F | 50 Mandatory | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `4E`.
