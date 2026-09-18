---
id: registry:L3:UA
kind: class
title: UA Urban area
system: registry:L3
code: UA
name: Urban area
status: registered
decomposed: true
file_class_id: '2'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_Building
links:
- rel: in_system
  id: registry:L3
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
sources:
- okf/registry/_raw/L3/L3.lccs
schema: okf/0.1
---

# UA Urban area

## Definition (verbatim, FAO LCLR)

Urban and/or rural settlement

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3 | 4 Mandatory | `LC_Building` | Mandatory | 20.0–100.0 |  | LC_ConstructionUse (type=Residential) |

Full rows: `../elements.csv`, class_id `2`.
