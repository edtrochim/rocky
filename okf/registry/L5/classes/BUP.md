---
id: registry:L5:BUP
kind: class
title: BUP Built-up
system: registry:L5
code: BUP
name: Built-up
status: registered
decomposed: true
file_class_id: 3E
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_NonLinearSurface
links:
- rel: in_system
  id: registry:L5
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_NonLinearSurface
  path: ../../../vocab/elements/LC_NonLinearSurface.md
sources:
- okf/registry/_raw/L5/L5.lccs
schema: okf/0.1
---

# BUP Built-up

## Definition (verbatim, FAO LCLR)

The land covered by buildings, roads and artificial surfaced ar-eas. Different types of build-up are included in this class (i.e. urban, airports, oilfields). Non-vegetated areas are character-ized by NDVI values close to zero.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3F | 40 Mandatory | `LC_NonLinearSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `3E`.
