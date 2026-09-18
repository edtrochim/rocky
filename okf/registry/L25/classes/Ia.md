---
id: registry:L25:Ia
kind: class
title: Ia Industrial and other
system: registry:L25
code: Ia
name: Industrial and other
status: registered
decomposed: true
file_class_id: 2F6
n_rows: 28
rows_in: ../elements.csv
element_refs:
- LC_OtherArtificialSurface
- LC_OtherConstruction
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_OtherArtificialSurface
  path: ../../../vocab/elements/LC_OtherArtificialSurface.md
- rel: uses_type
  id: element:LC_OtherConstruction
  path: ../../../vocab/elements/LC_OtherConstruction.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Ia Industrial and other

## Definition (verbatim, FAO LCLR)

Artificial surfaces including industrial areas and other artificial surfaces.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2F7 | 2F8 Mandatory | `LC_OtherConstruction` | Mandatory |  |  | LC_ConstructionUse (type=Industrial) |
| 2FB | 2FC Mandatory | `LC_OtherArtificialSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `2F6`.
