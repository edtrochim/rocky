---
id: registry:L25:Ahms
kind: class
title: Ahms Salt marsh
system: registry:L25
code: Ahms
name: Salt marsh
status: registered
decomposed: true
file_class_id: '179'
n_rows: 46
rows_in: ../elements.csv
element_refs:
- LC_GrowthForm
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L25
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
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Ahms Salt marsh

## Definition (verbatim, FAO LCLR)

This class is very basic, and generic being constituted by two mandatory stratum that defines the overall class structure i.e., herbaceous growth form and water body with brakish water salinity.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 17A | 182 Optional | `LC_GrowthForm` | Mandatory | 1.0–10.0 |  | LC_VegetationArtificialityCharacteristic |
| 17A | 17B Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 20.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 17A | 17E Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Brackish) |

Full rows: `../elements.csv`, class_id `179`.
