---
id: registry:L25:A
kind: class
title: A Tree dominated area
system: registry:L25
code: A
name: Tree dominated area
status: registered
decomposed: true
file_class_id: '41'
n_rows: 40
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L25
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
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# A Tree dominated area

## Definition (verbatim, FAO LCLR)

It corresponds to areas with natural semi-natural vegetation where the growth form tree is dominant. The cover % of the element tree is >20% (cover ranging from 20 to 100%). The presence of other woody (shrubs) or non woody (herbs) growth forms is recognized with any cover percentage.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 42 | 43 Mandatory | `LC_Tree` | Mandatory | 20.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 42 | 46 Mandatory | `LC_Shrub` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 42 | 49 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `41`.
