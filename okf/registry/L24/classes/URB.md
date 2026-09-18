---
id: registry:L24:URB
kind: class
title: URB Urban areas
system: registry:L24
code: URB
name: Urban areas
status: registered
decomposed: true
file_class_id: 1C
n_rows: 15
rows_in: ../elements.csv
element_refs:
- LC_ArtificialSurfaceElement
links:
- rel: in_system
  id: registry:L24
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_ArtificialSurfaceElement
  path: ../../../vocab/elements/LC_ArtificialSurfaceElement.md
sources:
- okf/registry/_raw/L24/L24.lccs
schema: okf/0.1
---

# URB Urban areas

## Definition (verbatim, FAO LCLR)

Urban areas

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1D | 1E Mandatory | `LC_ArtificialSurfaceElement` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `1C`.
