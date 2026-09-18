---
id: registry:L25:Vr
kind: class
title: Vr Rural villages
system: registry:L25
code: Vr
name: Rural villages
status: registered
decomposed: true
file_class_id: 2E3
n_rows: 27
rows_in: ../elements.csv
element_refs:
- LC_Building
- LC_OtherArtificialSurface
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
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Vr Rural villages

## Definition (verbatim, FAO LCLR)

Artificial surfaces with rural area geographical aspect including buildings and other artificial surfaces.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2E5 | 2E6 Mandatory | `LC_Building` | Mandatory |  |  |  |
| 2E8 | 2E9 Mandatory | `LC_OtherArtificialSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `2E3`.
