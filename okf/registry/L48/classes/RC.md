---
id: registry:L48:RC
kind: class
title: RC Rainfed crops
system: registry:L48
code: RC
name: Rainfed crops
status: registered
decomposed: true
file_class_id: '9'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L48
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L48/L48.lccs
schema: okf/0.1
---

# RC Rainfed crops

## Definition (verbatim, FAO LCLR)

Cropland where the water source depends on the rainwater. Most of the crops planted are herbaceous main crops or source of carbohydrate. The most common cultivated crops in this category are wheat, sorghum, barley, maize, and safflower. The main rain-fed crops are wheat, and barley, cultivated in winter season.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| A | B Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed) |

Full rows: `../elements.csv`, class_id `9`.
