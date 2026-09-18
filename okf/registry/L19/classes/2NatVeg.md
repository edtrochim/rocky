---
id: registry:L19:2NatVeg
kind: class
title: 2NatVeg Natural vegetation
system: registry:L19
code: 2NatVeg
name: Natural vegetation
status: registered
decomposed: true
file_class_id: '69'
n_rows: 28
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L19
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L19/L19.lccs
schema: okf/0.1
---

# 2NatVeg Natural vegetation

## Definition (verbatim, FAO LCLR)

Natural And Semi-Natural Primarily Terrestrial Vegetation.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 6A | 6B Mandatory | `LC_Shrub` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 6A | 6E Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `69`.
