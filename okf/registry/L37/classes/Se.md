---
id: registry:L37:Se
kind: class
title: Se Water surface
system: registry:L37
code: Se
name: Water surface
status: registered
decomposed: true
file_class_id: '116'
n_rows: 13
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L37
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L37/L37.LChS
schema: okf/0.1
---

# Se Water surface

## Definition (verbatim, FAO LCLR)

They represent the courses followed by the continuous natural flow of water on the surface of the ground and draining a given sector. Included in this class are natural and artificial watercourses that serve as water flow channels, including canals. Width to take into account: 100 m. Lakes, ponds, natural ponds and dam reservoirs are included in this class.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 117 | 118 Mandatory | `LC_WaterBody` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `116`.
