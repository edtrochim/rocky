---
id: registry:L25:Ep
kind: class
title: Ep Erg (dunes) parabolic
system: registry:L25
code: Ep
name: Erg (dunes) parabolic
status: registered
decomposed: true
file_class_id: 2CD
n_rows: 15
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

# Ep Erg (dunes) parabolic

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of dunes. It is constituted by one mandatory stratum that defines the overall class structure. The strata is constituted by one basic element dune with parabolic type.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2CE | 2CF Mandatory | `LC_Dune` | Mandatory |  | type=Parabolic |  |

Full rows: `../elements.csv`, class_id `2CD`.
