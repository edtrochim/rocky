---
id: registry:L25:Er
kind: class
title: Er Erg (dunes)
system: registry:L25
code: Er
name: Erg (dunes)
status: registered
decomposed: true
file_class_id: 2C1
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

# Er Erg (dunes)

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of dunes. It is constituted by one mandatory stratum that defines the overall class structure. The strata is constituted by one basic element dune.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2C2 | 2C3 Mandatory | `LC_Dune` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `2C1`.
