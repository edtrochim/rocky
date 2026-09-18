---
id: registry:L34:Sv
kind: class
title: Sv Spare vegetation
system: registry:L34
code: Sv
name: Spare vegetation
status: registered
decomposed: true
file_class_id: '16'
n_rows: 28
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L34
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L34/L34.lccs
schema: okf/0.1
---

# Sv Spare vegetation

## Definition (verbatim, FAO LCLR)

This land is categorized by bare soil which is sparsely populated with shrubs and grasses. This land is unmanaged and is not used for cultivation or grazing purposes.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 17 | 18 Mandatory | `LC_Shrub` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 17 | 1B Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `16`.
