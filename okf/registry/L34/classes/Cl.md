---
id: registry:L34:Cl
kind: class
title: Cl Cultivated land
system: registry:L34
code: Cl
name: Cultivated land
status: registered
decomposed: true
file_class_id: D
n_rows: 17
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

# Cl Cultivated land

## Definition (verbatim, FAO LCLR)

This land consists of agricultural fields which may feature various types of crops such as wheat and barley, horticultural crops (e.g. tomatoes and potatoes), legumes and forage crops. The crop water management in these areas may be irrigated or rainfed.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| E | F Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `D`.
