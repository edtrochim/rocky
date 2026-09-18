---
id: registry:L7:Ds
kind: class
title: Ds Extraxtion Sites (Mine/Quarry)
system: registry:L7
code: Ds
name: Extraxtion Sites (Mine/Quarry)
status: registered
decomposed: true
file_class_id: A2
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_NonBuiltUpSurface
links:
- rel: in_system
  id: registry:L7
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_NonBuiltUpSurface
  path: ../../../vocab/elements/LC_NonBuiltUpSurface.md
sources:
- okf/registry/_raw/L7/L7.lccs
schema: okf/0.1
---

# Ds Extraxtion Sites (Mine/Quarry)

## Definition (verbatim, FAO LCLR)

Absence of the original natural (semi-natural) cover or water surface and land cover, rock or earthy materials are removed by human activity

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| A3 | A4 Mandatory | `LC_NonBuiltUpSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `A2`.
