---
id: registry:L14:TRC
kind: class
title: TRC Terraced rainfed crop
system: registry:L14
code: TRC
name: Terraced rainfed crop
status: registered
decomposed: true
file_class_id: 2B
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L14
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L14/L14.lccs
schema: okf/0.1
---

# TRC Terraced rainfed crop

## Definition (verbatim, FAO LCLR)

Terraced Rainfed crops in sloping land

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2C | 2D Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_MechanicalErosionControl]/name=Mechanical Erosion Control) |

Full rows: `../elements.csv`, class_id `2B`.
