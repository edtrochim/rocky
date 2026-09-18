---
id: registry:L32:Ac
kind: class
title: Ac Annual crop
system: registry:L32
code: Ac
name: Annual crop
status: registered
decomposed: true
file_class_id: '31'
n_rows: 20
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L32
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L32/L32.lccs
schema: okf/0.1
---

# Ac Annual crop

## Definition (verbatim, FAO LCLR)

Annual cultivated and managed vegetation on flat land.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 32 | 33 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_CropRotation]/name=Crop Rotation, elements/LC_Characteristic[LC_CropRotation]/description=Describe the crop rotation) |

Full rows: `../elements.csv`, class_id `31`.
