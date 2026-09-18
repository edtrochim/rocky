---
id: registry:L32:Pr
kind: class
title: Pr Paddy rice
system: registry:L32
code: Pr
name: Paddy rice
status: registered
decomposed: true
file_class_id: 2A
n_rows: 21
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L32
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L32/L32.lccs
schema: okf/0.1
---

# Pr Paddy rice

## Definition (verbatim, FAO LCLR)

Single season paddy rice/ rotation paddy-annual crops/ upland rice with rainfed and irrigated.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2B | 2C Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation, elements/LC_Characteristic[LC_Rainfed]/name=Rainfed) |

Full rows: `../elements.csv`, class_id `2A`.
