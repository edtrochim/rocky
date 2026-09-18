---
id: registry:L38:HCIR
kind: class
title: HCIR Herbaceous crop irrigated
system: registry:L38
code: HCIR
name: Herbaceous crop irrigated
status: registered
decomposed: true
file_class_id: 2CD
n_rows: 32
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L38
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L38/L38.lccs
schema: okf/0.1
---

# HCIR Herbaceous crop irrigated

## Definition (verbatim, FAO LCLR)

Irrigated cultivation (herbaceous, shrub and tree crops)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2CE | 2CF Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation) |
| 2CE | 2D3 Mandatory | `LC_WoodyGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation) |

Full rows: `../elements.csv`, class_id `2CD`.
