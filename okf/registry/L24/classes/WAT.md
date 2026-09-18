---
id: registry:L24:WAT
kind: class
title: WAT Water bodies
system: registry:L24
code: WAT
name: Water bodies
status: registered
decomposed: true
file_class_id: '17'
n_rows: 20
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L24
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L24/L24.lccs
schema: okf/0.1
---

# WAT Water bodies

## Definition (verbatim, FAO LCLR)

Seasonal/perennial, natural/artificial Water bodies.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 18 | 19 Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Flowing / Standing | LC_ArtificialityCharacteristic (type=Natural / Artificial) |

Full rows: `../elements.csv`, class_id `17`.
