---
id: registry:L7:Vbr
kind: class
title: Vbr Volcanic rocks
system: registry:L7
code: Vbr
name: Volcanic rocks
status: registered
decomposed: true
file_class_id: '88'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_BareRock
links:
- rel: in_system
  id: registry:L7
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareRock
  path: ../../../vocab/elements/LC_BareRock.md
sources:
- okf/registry/_raw/L7/L7.lccs
schema: okf/0.1
---

# Vbr Volcanic rocks

## Definition (verbatim, FAO LCLR)

Lands with exposed rocks, that never have more than 4% vegetated cover during any time of the year.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 89 | 8A Mandatory | `LC_BareRock` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `88`.
