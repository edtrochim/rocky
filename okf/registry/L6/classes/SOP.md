---
id: registry:L6:SOP
kind: class
title: SOP Shrubs sparse natural vegetation
system: registry:L6
code: SOP
name: Shrubs sparse natural vegetation
status: registered
decomposed: true
file_class_id: 2E
n_rows: 29
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L6
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L6/L6.lccs
schema: okf/0.1
---

# SOP Shrubs sparse natural vegetation

## Definition (verbatim, FAO LCLR)

Natural open shrubs, occasionally with sparse or closed herbaceous vegetation cover, with percentage cover varying from 10 to 60%.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2F | 30 Mandatory | `LC_Shrub` | Mandatory | 10.0–60.0 |  | LC_VegetationArtificialityCharacteristic |
| 2F | 33 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `2E`.
