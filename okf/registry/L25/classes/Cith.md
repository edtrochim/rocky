---
id: registry:L25:Cith
kind: class
title: Cith Shifting herb cultivation
system: registry:L25
code: Cith
name: Shifting herb cultivation
status: registered
decomposed: true
file_class_id: 1EF
n_rows: 39
rows_in: ../elements.csv
element_refs:
- LC_GrowthForm
- LC_HerbaceousGrowthForm
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
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Cith Shifting herb cultivation

## Definition (verbatim, FAO LCLR)

This class is very basic, and generic being constituted by one mandatory stratum that defines the overall class structure. It is rainfed plantation area with rotational period from 1 to 2 years with cover percentage of 15-30%.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1F0 | 1F1 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_CropRotation]/name=Crop Rotation) |
| 1F6 | 1F7 Mandatory | `LC_GrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `1EF`.
