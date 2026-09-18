---
id: registry:L7:Bs
kind: class
title: Bs Bare soil
system: registry:L7
code: Bs
name: Bare soil
status: registered
decomposed: true
file_class_id: 9E
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
links:
- rel: in_system
  id: registry:L7
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
sources:
- okf/registry/_raw/L7/L7.lccs
schema: okf/0.1
---

# Bs Bare soil

## Definition (verbatim, FAO LCLR)

Lands with exposed soil, that never have more than 4% vegetated cover during any time of the year.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 9F | A0 Mandatory | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `9E`.
