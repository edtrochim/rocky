---
id: registry:L38:CU1
kind: class
title: CU1 Mixed unit (herbaceous crop rainfed - natural vegetation - settlements)
system: registry:L38
code: CU1
name: Mixed unit (herbaceous crop rainfed - natural vegetation - settlements)
status: registered
decomposed: true
file_class_id: 1B2
n_rows: 47
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

# CU1 Mixed unit (herbaceous crop rainfed - natural vegetation - settlements)

## Definition (verbatim, FAO LCLR)

Areas principally occupied by small crop fields interspersed in a significant fraction of natural vegetation. Rural settlements are also present

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 280 | 281 Mandatory | `LC_GrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 1B3 | 1B4 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 10.0–50.0 |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_FieldSize]/name=Field Size) |
| 24B | 24C Optional | `LC_Building` | Mandatory |  | construction_material=Light Material |  |

Full rows: `../elements.csv`, class_id `1B2`.
