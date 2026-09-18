---
id: registry:L25:Ae
kind: class
title: Ae Airport
system: registry:L25
code: Ae
name: Airport
status: registered
decomposed: true
file_class_id: 31A
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

# Ae Airport

## Definition (verbatim, FAO LCLR)

It is a built-up nonlinear area which is used for flights to take off and land.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 31B | 31C Mandatory | `LC_OtherConstruction` | Mandatory |  |  | LC_ConstructionUse (type=Airport) |
| 31F | 320 Mandatory | `LC_OtherArtificialSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `31A`.
