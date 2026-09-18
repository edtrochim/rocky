---
id: registry:L2:1HI
kind: class
title: 1HI Irrigated herbaceous crops
system: registry:L2
code: 1HI
name: Irrigated herbaceous crops
status: registered
decomposed: true
file_class_id: '9'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L2
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L2/L2.lccs
schema: okf/0.1
---

# 1HI Irrigated herbaceous crops

## Definition (verbatim, FAO LCLR)

Irrigated herbaceous crops

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| A | B Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation) |

Full rows: `../elements.csv`, class_id `9`.
