---
id: registry:L25:El
kind: class
title: El Erg (dunes) longitudinal
system: registry:L25
code: El
name: Erg (dunes) longitudinal
status: registered
decomposed: true
file_class_id: 2C5
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_Dune
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Dune
  path: ../../../vocab/elements/LC_Dune.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# El Erg (dunes) longitudinal

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of dunes. It is constituted by one mandatory stratum that defines the overall class structure. The strata is constituted by one basic element dune with longitudinal type.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2C6 | 2C7 Mandatory | `LC_Dune` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `2C5`.
