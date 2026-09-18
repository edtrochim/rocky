---
id: registry:L12:RH1
kind: class
title: RH1 Rural settlements (plain area)
system: registry:L12
code: RH1
name: Rural settlements (plain area)
status: registered
decomposed: true
file_class_id: '11'
n_rows: 43
rows_in: ../elements.csv
element_refs:
- LC_Building
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# RH1 Rural settlements (plain area)

## Definition (verbatim, FAO LCLR)

Rural houses in flat lying plain areas (slop up to 5 degrees) + small cultivated herbaceous crops + closed herbaceous natural vegetation, often together with trees and/or shrubs employed for demarcation; scattered open areas observed in some areas.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 12 | 13 Mandatory | `LC_Building` | Mandatory | 5.0–10.0 |  | LC_ConstructionUse (type=Residential-rural) |
| 12 | 13 Mandatory | `LC_HerbaceousGrowthForm` | Optional |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_FieldSize]/name=Field Size, elements/LC_Characteristic[LC_FieldSize]/description=Describe the field size) |
| 12 | 13 Mandatory | `LC_HerbaceousGrowthForm` | Optional |  |  | LC_VegetationArtificialityCharacteristic; LC_GrazedCharacteristic (elements/LC_Characteristic[LC_GrazingAnimalType]/name=Grazing Animal, elements/LC_Characteristic[LC_GrazingAnimalType]/description=Describe the grazing animal, elements/LC_Characteristic[LC_GrazingAnimalType]/animal_type=Domestic livestoc) |

Full rows: `../elements.csv`, class_id `11`.
