---
id: registry:L45:Canh
kind: class
title: Canh Annual herb cultivation
system: registry:L45
code: Canh
name: Annual herb cultivation
status: registered
decomposed: true
file_class_id: '78'
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L45
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L45/L45.lccs
schema: okf/0.1
---

# Canh Annual herb cultivation

## Definition (verbatim, FAO LCLR)

Lands covered with temporary rainfed herbaceous crops followed by harvest and a bare soil period.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 79 | 7A Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_CropRotation]/name=Crop Rotation, elements/LC_Characteristic[LC_CropRotation]/description=Describe the crop rotation, elements/LC_Characteristic[LC_Rainfed]/name=Rainfed) |

Full rows: `../elements.csv`, class_id `78`.
