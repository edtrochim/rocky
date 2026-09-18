---
id: registry:L13:AGa
kind: class
title: AGa Cultivated Aquatic or Regularly Flooded Area(s)
system: registry:L13
code: AGa
name: Cultivated Aquatic or Regularly Flooded Area(s)
status: registered
decomposed: true
file_class_id: 2C
n_rows: 33
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L13
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L13/L13.lccs
schema: okf/0.1
---

# AGa Cultivated Aquatic or Regularly Flooded Area(s)

## Definition (verbatim, FAO LCLR)

Small sized ( < 2 Ha) fields of rice flooded for more than 9 months.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2D | 31 Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Fresh) |
| 2D | 2E Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `2C`.
