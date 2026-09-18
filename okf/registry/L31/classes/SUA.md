---
id: registry:L31:SUA
kind: class
title: SUA Scattered urban area
system: registry:L31
code: SUA
name: Scattered urban area
status: registered
decomposed: true
file_class_id: '40'
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

# SUA Scattered urban area

## Definition (verbatim, FAO LCLR)

Areas with allotted low-density residential and commercial housing. Constructions are sparse, separated with more than 5 meters.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 41 | 42 Mandatory | `LC_Building` | Mandatory | 20.0–50.0 | construction_material=Hard Material |  |
| 41 | 44 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 20.0–80.0 |  | LC_CultivatedAndManagedVegetationCharacteristics |
| 41 | 47 Optional | `LC_Tree` | Mandatory | 0.0–50.0 |  | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `40`.
