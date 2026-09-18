---
id: registry:L7:Ai
kind: class
title: Ai Airports
system: registry:L7
code: Ai
name: Airports
status: registered
decomposed: true
file_class_id: C1
n_rows: 28
rows_in: ../elements.csv
element_refs:
- LC_OtherArtificialSurface
- LC_OtherConstruction
links:
- rel: in_system
  id: registry:L7
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_OtherArtificialSurface
  path: ../../../vocab/elements/LC_OtherArtificialSurface.md
- rel: uses_type
  id: element:LC_OtherConstruction
  path: ../../../vocab/elements/LC_OtherConstruction.md
sources:
- okf/registry/_raw/L7/L7.lccs
schema: okf/0.1
---

# Ai Airports

## Definition (verbatim, FAO LCLR)

Built-up areas with facilities for flights to take off and land.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| C2 | C3 Mandatory | `LC_OtherConstruction` | Mandatory |  |  | LC_ConstructionUse (type=Airport) |
| C6 | C7 Mandatory | `LC_OtherArtificialSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `C1`.
