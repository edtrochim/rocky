---
id: registry:L43:Nst
kind: class
title: Nst Natural surfaces
system: registry:L43
code: Nst
name: Natural surfaces
status: registered
decomposed: true
file_class_id: '46'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_NaturalSurfaceElement
links:
- rel: in_system
  id: registry:L43
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_NaturalSurfaceElement
  path: ../../../vocab/elements/LC_NaturalSurfaceElement.md
sources:
- okf/registry/_raw/L43/L43.lccs
schema: okf/0.1
---

# Nst Natural surfaces

## Definition (verbatim, FAO LCLR)

Areas dominated by soil, sand and rock surfaces.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 47 | 48 Mandatory | `LC_NaturalSurfaceElement` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `46`.
