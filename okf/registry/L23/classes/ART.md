---
id: registry:L23:ART
kind: class
title: ART Artificial surface
system: registry:L23
code: ART
name: Artificial surface
status: registered
decomposed: true
file_class_id: 1B
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_BuiltUpSurface
links:
- rel: in_system
  id: registry:L23
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BuiltUpSurface
  path: ../../../vocab/elements/LC_BuiltUpSurface.md
sources:
- okf/registry/_raw/L23/L23.lccs
schema: okf/0.1
---

# ART Artificial surface

## Definition (verbatim, FAO LCLR)

Built-up land, including populated places, industrial sites, major roads, and extraction sites.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1C | 1D Mandatory | `LC_BuiltUpSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `1B`.
