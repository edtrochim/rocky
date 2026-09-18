---
id: registry:L7:UA
kind: class
title: UA Urban Areas
system: registry:L7
code: UA
name: Urban Areas
status: registered
decomposed: true
file_class_id: A6
n_rows: 37
rows_in: ../elements.csv
element_refs:
- LC_Building
- LC_OtherArtificialSurface
- LC_OtherConstruction
links:
- rel: in_system
  id: registry:L7
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
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

# UA Urban Areas

## Definition (verbatim, FAO LCLR)

Artificial surfaces with urban area geographical aspect including buildings, other constructions, and other artificial surfaces.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| A8 | A9 Mandatory | `LC_Building` | Mandatory |  |  |  |
| AB | AC Mandatory | `LC_OtherConstruction` | Mandatory |  |  |  |
| AE | AF Mandatory | `LC_OtherArtificialSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `A6`.
