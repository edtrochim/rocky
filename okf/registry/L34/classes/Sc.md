---
id: registry:L34:Sc
kind: class
title: Sc Sugarcane
system: registry:L34
code: Sc
name: Sugarcane
status: registered
decomposed: true
file_class_id: '26'
n_rows: 23
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L34
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L34/L34.lccs
schema: okf/0.1
---

# Sc Sugarcane

## Definition (verbatim, FAO LCLR)

This class consists of agricultural land which is used for the cultivation of sugarcane.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 27 | 28 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics; LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_SinglePlantSpecies]/name=Single Plant Species, elements/LC_Characteristic[LC_SinglePlantSpecies]/description=Describe a floristic aspect of single plant species, elements/LC_Characteristic[LC_SinglePlantSpecies]/type=Sugarcane) |

Full rows: `../elements.csv`, class_id `26`.
