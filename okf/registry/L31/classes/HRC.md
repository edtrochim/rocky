---
id: registry:L31:HRC
kind: class
title: HRC Herbaceous rainfed cropland
system: registry:L31
code: HRC
name: Herbaceous rainfed cropland
status: registered
decomposed: true
file_class_id: '2'
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L31
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L31/L31.lccs
schema: okf/0.1
---

# HRC Herbaceous rainfed cropland

## Definition (verbatim, FAO LCLR)

Areas covered with herbaceous rainfed agricultural crops, mainly maize, cassava and beans, with parcels of 1 Ha on average. Main cropping seasons goes from September to March.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3 | 4 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_FieldSize]/description=Describe the field size) |

Full rows: `../elements.csv`, class_id `2`.
