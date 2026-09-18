---
id: registry:L24:BS
kind: class
title: BS Bare rocks and soils
system: registry:L24
code: BS
name: Bare rocks and soils
status: registered
decomposed: true
file_class_id: '20'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_NaturalSurfaceElement
links:
- rel: in_system
  id: registry:L24
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_NaturalSurfaceElement
  path: ../../../vocab/elements/LC_NaturalSurfaceElement.md
sources:
- okf/registry/_raw/L24/L24.lccs
schema: okf/0.1
---

# BS Bare rocks and soils

## Definition (verbatim, FAO LCLR)

Bare rocks and soils and/or other unconsolidated material(s).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 21 | 22 Mandatory | `LC_NaturalSurfaceElement` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `20`.
