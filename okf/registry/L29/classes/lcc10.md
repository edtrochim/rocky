---
id: registry:L29:lcc10
kind: class
title: lcc10 Bare soil
system: registry:L29
code: lcc10
name: Bare soil
status: registered
decomposed: true
file_class_id: '68'
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_Dune
links:
- rel: in_system
  id: registry:L29
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_Dune
  path: ../../../vocab/elements/LC_Dune.md
sources:
- okf/registry/_raw/L29/L29.lccs
schema: okf/0.1
---

# lcc10 Bare soil

## Definition (verbatim, FAO LCLR)

A soil surface devoid of any plant material.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 69 | 6A Mandatory | `LC_BareSoil` | Mandatory |  |  |  |
| 69 | 6A Mandatory | `LC_Dune` | Optional |  |  |  |

Full rows: `../elements.csv`, class_id `68`.
