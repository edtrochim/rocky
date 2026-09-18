---
id: registry:L11:GR
kind: class
title: GR Grassland
system: registry:L11
code: GR
name: Grassland
status: registered
decomposed: true
file_class_id: 8F
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L11
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L11/L11.lccs
schema: okf/0.1
---

# GR Grassland

## Definition (verbatim, FAO LCLR)

Relatively dense herbaceous natural vegetation, occasionally with sparse shrubs.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 90 | 91 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 1.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 90 | 91 Mandatory | `LC_Shrub` | Optional |  |  |  |

Full rows: `../elements.csv`, class_id `8F`.
