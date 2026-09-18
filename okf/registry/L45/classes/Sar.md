---
id: registry:L45:Sar
kind: class
title: Sar Shrub savanna
system: registry:L45
code: Sar
name: Shrub savanna
status: registered
decomposed: true
file_class_id: '28'
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L45
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L45/L45.lccs
schema: okf/0.1
---

# Sar Shrub savanna

## Definition (verbatim, FAO LCLR)

Lands with herbaceous types of cover. Shrub cover between 4–20%.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 29 | 2A Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 40.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 29 | 2D Mandatory | `LC_Shrub` | Mandatory | 4.0–20.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `28`.
