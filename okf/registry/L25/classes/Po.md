---
id: registry:L25:Po
kind: class
title: Po Port
system: registry:L25
code: Po
name: Port
status: registered
decomposed: true
file_class_id: '312'
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

# Po Port

## Definition (verbatim, FAO LCLR)

It is a built up – nonlinear area for ships.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 313 | 314 Mandatory | `LC_OtherConstruction` | Mandatory |  |  | LC_ConstructionUse (type=Port Area) |
| 317 | 318 Mandatory | `LC_OtherArtificialSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `312`.
