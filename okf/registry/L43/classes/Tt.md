---
id: registry:L43:Tt
kind: class
title: Tt Tree-dominated area (terrestiral)
system: registry:L43
code: Tt
name: Tree-dominated area (terrestiral)
status: registered
decomposed: true
file_class_id: '6'
n_rows: 40
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L43
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L43/L43.lccs
schema: okf/0.1
---

# Tt Tree-dominated area (terrestiral)

## Definition (verbatim, FAO LCLR)

It corresponds to areas with natural semi-natural vegetation where the growth form tree is dominant.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 7 | 8 Mandatory | `LC_Tree` | Mandatory | 20.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 7 | B Optional | `LC_Shrub` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 7 | E Optional | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `6`.
