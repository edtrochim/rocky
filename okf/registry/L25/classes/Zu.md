---
id: registry:L25:Zu
kind: class
title: Zu Urban areas
system: registry:L25
code: Zu
name: Urban areas
status: registered
decomposed: true
file_class_id: 2EB
n_rows: 37
rows_in: ../elements.csv
element_refs:
- LC_Building
- LC_OtherArtificialSurface
- LC_OtherConstruction
links:
- rel: in_system
  id: registry:L25
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
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Zu Urban areas

## Definition (verbatim, FAO LCLR)

Artificial surfaces with urban area geographical aspect including buildings, other constructions and other artificial surfaces.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2ED | 2EE Mandatory | `LC_Building` | Mandatory |  |  |  |
| 2F0 | 2F1 Mandatory | `LC_OtherConstruction` | Mandatory |  |  |  |
| 2F3 | 2F4 Mandatory | `LC_OtherArtificialSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `2EB`.
