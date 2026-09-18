---
id: registry:L38:CU
kind: class
title: CU Mixed unit (settlements - natural vegetation - herbaceous crop rainfed)
system: registry:L38
code: CU
name: Mixed unit (settlements - natural vegetation - herbaceous crop rainfed)
status: registered
decomposed: true
file_class_id: '251'
n_rows: 53
rows_in: ../elements.csv
element_refs:
- LC_Building
- LC_GrowthForm
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L38
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
- rel: uses_type
  id: element:LC_GrowthForm
  path: ../../../vocab/elements/LC_GrowthForm.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L38/L38.lccs
schema: okf/0.1
---

# CU Mixed unit (settlements - natural vegetation - herbaceous crop rainfed)

## Definition (verbatim, FAO LCLR)

Areas principally occupied by rural settlements areas interspersed in a significant fraction of natural vegetation. Small cultivated crops and/or orchards are present

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 252 | 253 Mandatory | `LC_Building` | Mandatory | 0.0–50.0 | construction_material=Light Material | LC_ConstructionUse (type=Small buildings associated to rural areas) |
| 256 | 257 Optional | `LC_HerbaceousGrowthForm` | Mandatory | 0.0–20.0 |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_FieldSize]/name=Field Size) |
| 25C | 25D Mandatory | `LC_GrowthForm` | Mandatory | 40.0–80.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `251`.
