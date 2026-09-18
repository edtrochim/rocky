---
id: registry:L41:As
kind: class
title: As Articial Surface
system: registry:L41
code: As
name: Articial Surface
status: registered
decomposed: true
file_class_id: A6
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_ArtificialSurfaceElement
links:
- rel: in_system
  id: registry:L41
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_ArtificialSurfaceElement
  path: ../../../vocab/elements/LC_ArtificialSurfaceElement.md
sources:
- okf/registry/_raw/L41/L41.lccs
schema: okf/0.1
---

# As Articial Surface

## Definition (verbatim, FAO LCLR)

Built-up areas with residential, commercial, or industrial structures and related infrastructure. All artficial surfaces such as airports and dams

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| A8 | A9 Mandatory | `LC_ArtificialSurfaceElement` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `A6`.
