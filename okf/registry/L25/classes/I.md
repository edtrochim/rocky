---
id: registry:L25:I
kind: class
title: I Infrastructure
system: registry:L25
code: I
name: Infrastructure
status: registered
decomposed: true
file_class_id: 2FE
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

# I Infrastructure

## Definition (verbatim, FAO LCLR)

Artificial surfaces including infrastructure and other artificial surfaces.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 303 | 304 Mandatory | `LC_OtherArtificialSurface` | Mandatory |  |  |  |
| 2FF | 300 Mandatory | `LC_OtherConstruction` | Mandatory |  |  | LC_ConstructionUse (type=Infrastructures) |

Full rows: `../elements.csv`, class_id `2FE`.
