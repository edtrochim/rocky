---
id: registry:L35:Ai
kind: class
title: Ai Airport
system: registry:L35
code: Ai
name: Airport
status: registered
decomposed: true
file_class_id: '105'
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_Building
links:
- rel: in_system
  id: registry:L35
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
sources:
- okf/registry/_raw/L35/L35.lccs
schema: okf/0.1
---

# Ai Airport

## Definition (verbatim, FAO LCLR)

NA

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 106 | 107 Mandatory | `LC_Building` | Mandatory |  |  | LC_ConstructionUse (type=Airport) |

Full rows: `../elements.csv`, class_id `105`.
