---
id: registry:L45:Ahms
kind: class
title: Ahms Swamps
system: registry:L45
code: Ahms
name: Swamps
status: registered
decomposed: true
file_class_id: 4A
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

# Ahms Swamps

## Definition (verbatim, FAO LCLR)

Herbaceous or aquatic vegetation in permanent or semi-permanent wetlands and swamps. Water salinity is brackish.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 56 | 57 Optional | `LC_GrowthForm` | Mandatory | 1.0–10.0 |  | LC_VegetationArtificialityCharacteristic |
| 56 | 5A Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 20.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 56 | 5D Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_WaterSalinityCharacteristic (type=Brackish); LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `4A`.
