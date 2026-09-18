---
id: registry:L21:R
kind: class
title: R Rock
system: registry:L21
code: R
name: Rock
status: registered
decomposed: true
file_class_id: BC
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_BareRock
links:
- rel: in_system
  id: registry:L21
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareRock
  path: ../../../vocab/elements/LC_BareRock.md
sources:
- okf/registry/_raw/L21/L21.lccs
schema: okf/0.1
---

# R Rock

## Definition (verbatim, FAO LCLR)

Land of naturally exposed rocks or strip mines, quarries and gravel pits.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| BD | BE Mandatory | `LC_BareRock` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `BC`.
