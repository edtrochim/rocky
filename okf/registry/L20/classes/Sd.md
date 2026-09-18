---
id: registry:L20:Sd
kind: class
title: Sd Bare ground
system: registry:L20
code: Sd
name: Bare ground
status: registered
decomposed: true
file_class_id: B3
n_rows: 15
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
links:
- rel: in_system
  id: registry:L20
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
sources:
- okf/registry/_raw/L20/L20.lccs
schema: okf/0.1
---

# Sd Bare ground

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| B4 | B5 Mandatory | `LC_BareSoil` | Mandatory | 90.0–100.0 |  |  |

Full rows: `../elements.csv`, class_id `B3`.
