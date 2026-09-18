---
id: registry:L12:UA2
kind: class
title: UA2 Urban commercial and/or industrial
system: registry:L12
code: UA2
name: Urban commercial and/or industrial
status: registered
decomposed: true
file_class_id: C
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_Building
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# UA2 Urban commercial and/or industrial

## Definition (verbatim, FAO LCLR)

Commercial and/or industrial built-up areas, occasionally outside main urban and rural built-up areas.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| D | E Mandatory | `LC_Building` | Mandatory |  |  | LC_ConstructionUse (type=Commercial and/or Industrial) |

Full rows: `../elements.csv`, class_id `C`.
