---
id: registry:L6:WET
kind: class
title: WET Wetland
system: registry:L6
code: WET
name: Wetland
status: registered
decomposed: true
file_class_id: 7B
n_rows: 23
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L6
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L6/L6.lccs
schema: okf/0.1
---

# WET Wetland

## Definition (verbatim, FAO LCLR)

Wetlands are herbaceous vegetation with cover rang-ing from 60% to 100% found in flooded/wet areas, some-times associated with shrubs. NDVI values are higher during the summer season when the progressive reduction of water surface leaves space to the natural vegetation growth.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 7C | 7D Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  |  |
| 7C | 7F Mandatory | `LC_WaterBody` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `7B`.
