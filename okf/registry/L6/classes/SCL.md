---
id: registry:L6:SCL
kind: class
title: SCL Shrubs dense natural vegetation
system: registry:L6
code: SCL
name: Shrubs dense natural vegetation
status: registered
decomposed: true
file_class_id: '26'
n_rows: 29
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L6
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L6/L6.lccs
schema: okf/0.1
---

# SCL Shrubs dense natural vegetation

## Definition (verbatim, FAO LCLR)

Natural closed shrubs with shrubs percent-age cover of more than 60%.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 27 | 28 Mandatory | `LC_Shrub` | Mandatory | 60.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 27 | 2B Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `26`.
