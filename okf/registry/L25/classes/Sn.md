---
id: registry:L25:Sn
kind: class
title: Sn Bare soil
system: registry:L25
code: Sn
name: Bare soil
status: registered
decomposed: true
file_class_id: 2D5
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Sn Bare soil

## Definition (verbatim, FAO LCLR)

This class is very basic, and generic being constituted by one mandatory stratum that defines the overall class structure. The strata are constituted by one basic element bare soil.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2D6 | 2D7 Mandatory | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `2D5`.
