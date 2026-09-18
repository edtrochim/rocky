---
id: registry:L38:HCO
kind: class
title: HCO Herbaceous closed to open (with sparse woody vegetation)
system: registry:L38
code: HCO
name: Herbaceous closed to open (with sparse woody vegetation)
status: registered
decomposed: true
file_class_id: 11B
n_rows: 42
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L38
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L38/L38.lccs
schema: okf/0.1
---

# HCO Herbaceous closed to open (with sparse woody vegetation)

## Definition (verbatim, FAO LCLR)

Relatively dense herbaceous natural vegetation occasionally with sparse shrubs

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 11C | 120 Optional | `LC_Tree` | Mandatory | 1.0–10.0 |  | LC_VegetationArtificialityCharacteristic |
| 11C | 123 Optional | `LC_Shrub` | Mandatory | 1.0–10.0 |  | LC_VegetationArtificialityCharacteristic |
| 11C | 11D Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 10.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `11B`.
