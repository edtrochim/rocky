---
id: registry:L45:V
kind: class
title: V Orchards
system: registry:L45
code: V
name: Orchards
status: registered
decomposed: true
file_class_id: 6D
n_rows: 34
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L45
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L45/L45.lccs
schema: okf/0.1
---

# V Orchards

## Definition (verbatim, FAO LCLR)

Lands covered with perennial rainfed woody crops land cover type.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 6E | 75 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |
| 6E | 6F Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_Plantation]/name=Plantation) |

Full rows: `../elements.csv`, class_id `6D`.
