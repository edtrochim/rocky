---
id: registry:L21:Ws
kind: class
title: Ws Woodshrub
system: registry:L21
code: Ws
name: Woodshrub
status: registered
decomposed: true
file_class_id: 5E
n_rows: 29
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L21
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L21/L21.lccs
schema: okf/0.1
---

# Ws Woodshrub

## Definition (verbatim, FAO LCLR)

Areas dominated by evergreen and deciduous woodland with a height less than 5 meters.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 5F | 60 Mandatory | `LC_Shrub` | Mandatory | 10.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 5F | 63 Optional | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `5E`.
