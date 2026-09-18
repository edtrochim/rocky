---
id: registry:L45:Ahm
kind: class
title: Ahm Salt marsh
system: registry:L45
code: Ahm
name: Salt marsh
status: registered
decomposed: true
file_class_id: '61'
n_rows: 46
rows_in: ../elements.csv
element_refs:
- LC_GrowthForm
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L45
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_GrowthForm
  path: ../../../vocab/elements/LC_GrowthForm.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L45/L45.lccs
schema: okf/0.1
---

# Ahm Salt marsh

## Definition (verbatim, FAO LCLR)

Herbaceous or aquatic vegetation in permanent or semi-permanent wetlands and swamps.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 62 | 63 Optional | `LC_GrowthForm` | Mandatory | 1.0–10.0 |  | LC_VegetationArtificialityCharacteristic |
| 62 | 66 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 20.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 62 | 69 Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_WaterSalinityCharacteristic (type=Fresh); LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `61`.
