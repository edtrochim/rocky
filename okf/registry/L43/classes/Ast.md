---
id: registry:L43:Ast
kind: class
title: Ast Artificial surfaces
system: registry:L43
code: Ast
name: Artificial surfaces
status: registered
decomposed: true
file_class_id: '26'
n_rows: 17
rows_in: ../elements.csv
element_refs:
- LC_ArtificialSurfaceElement
links:
- rel: in_system
  id: registry:L43
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_ArtificialSurfaceElement
  path: ../../../vocab/elements/LC_ArtificialSurfaceElement.md
sources:
- okf/registry/_raw/L43/L43.lccs
schema: okf/0.1
---

# Ast Artificial surfaces

## Definition (verbatim, FAO LCLR)

Areas dominated by buildings and infrastructure, including residential, industrial, and transportation surfaces.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 27 | 28 Mandatory | `LC_ArtificialSurfaceElement` | Mandatory |  |  | LC_ArtificialSurfaceTypes |

Full rows: `../elements.csv`, class_id `26`.
