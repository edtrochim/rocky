---
id: registry:L36:Cp
kind: class
title: Cp Other rainfed crop
system: registry:L36
code: Cp
name: Other rainfed crop
status: registered
decomposed: true
file_class_id: 1C8
n_rows: 27
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L36
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L36/L36.lccs
schema: okf/0.1
---

# Cp Other rainfed crop

## Definition (verbatim, FAO LCLR)

The land is covered by rainfed agricultural fields, featuring various types of crops: cereal crops such as wheat and barley, horticultural crops like tomatoes and melonds, legumes, and forage crops. The crop water management in these areas is rainfed.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1C9 | 1CA Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed) |
| 1C9 | 22C Optional | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `1C8`.
