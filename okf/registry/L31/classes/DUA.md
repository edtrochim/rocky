---
id: registry:L31:DUA
kind: class
title: DUA Dense urban area
system: registry:L31
code: DUA
name: Dense urban area
status: registered
decomposed: true
file_class_id: '36'
n_rows: 40
rows_in: ../elements.csv
element_refs:
- LC_Building
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L31
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L31/L31.lccs
schema: okf/0.1
---

# DUA Dense urban area

## Definition (verbatim, FAO LCLR)

Areas with allotted residential and commercial housing. Includes artificial surfaces and buildings. The distance between buildings and other constructions is less than 5 meters, with scattered vegetation (e.g., parks) and small backyard agriculture.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 37 | 38 Mandatory | `LC_Building` | Mandatory | 60.0–90.0 | construction_material=Hard Material |  |
| 37 | 3A Optional | `LC_Tree` | Mandatory | 0.0–10.0 |  | LC_CultivatedAndManagedVegetationCharacteristics |
| 37 | 3D Optional | `LC_HerbaceousGrowthForm` | Mandatory | 0.0–10.0 |  | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `36`.
