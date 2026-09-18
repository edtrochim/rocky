---
id: registry:L34:In
kind: class
title: In Infrastructure
system: registry:L34
code: In
name: Infrastructure
status: registered
decomposed: true
file_class_id: '2'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_ArtificialSurfaceElement
links:
- rel: in_system
  id: registry:L34
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_ArtificialSurfaceElement
  path: ../../../vocab/elements/LC_ArtificialSurfaceElement.md
sources:
- okf/registry/_raw/L34/L34.lccs
schema: okf/0.1
---

# In Infrastructure

## Definition (verbatim, FAO LCLR)

This land is characterized by the presence of buildings, roads and artificial surfaces. Different types of builtup areas can be included in this classs, such as urban areas, airports and oil fields.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3 | 4 Mandatory | `LC_ArtificialSurfaceElement` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `2`.
