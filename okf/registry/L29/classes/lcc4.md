---
id: registry:L29:lcc4
kind: class
title: lcc4 Water bodies
system: registry:L29
code: lcc4
name: Water bodies
status: registered
decomposed: true
file_class_id: '33'
n_rows: 53
rows_in: ../elements.csv
element_refs:
- LC_Algae
- LC_Moss
- LC_WaterBody
links:
- rel: in_system
  id: registry:L29
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Algae
  path: ../../../vocab/elements/LC_Algae.md
- rel: uses_type
  id: element:LC_Moss
  path: ../../../vocab/elements/LC_Moss.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L29/L29.lccs
schema: okf/0.1
---

# lcc4 Water bodies

## Definition (verbatim, FAO LCLR)

Rivers are natural flowing water bodies and typically have elongated shapes. Lakes and ponds are perennial standing water bodies.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 34 | 35 Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Flowing |  |
| 34 | 37 Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Standing |  |
| 34 | 39 Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Standing | LC_ArtificialityCharacteristic (type=Artificial) |
| 34 | 3E Mandatory | `LC_Moss` | Mandatory |  |  |  |
| 34 | 3E Mandatory | `LC_Algae` | Optional |  |  |  |
| 34 | 3E Mandatory | `LC_WaterBody` | Optional |  |  |  |

Full rows: `../elements.csv`, class_id `33`.
