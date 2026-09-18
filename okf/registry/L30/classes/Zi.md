---
id: registry:L30:Zi
kind: class
title: Zi Industrial zone
system: registry:L30
code: Zi
name: Industrial zone
status: registered
decomposed: true
file_class_id: '124'
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_NonLinearSurface
links:
- rel: in_system
  id: registry:L30
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_NonLinearSurface
  path: ../../../vocab/elements/LC_NonLinearSurface.md
sources:
- okf/registry/_raw/L30/L30.lccs
schema: okf/0.1
---

# Zi Industrial zone

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 125 | 126 Mandatory | `LC_NonLinearSurface` | Mandatory |  |  | LC_ConstructionUse (type=Industrial and/or commercial areas and/or infrastructures) |

Full rows: `../elements.csv`, class_id `124`.
