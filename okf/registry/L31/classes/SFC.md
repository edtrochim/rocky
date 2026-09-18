---
id: registry:L31:SFC
kind: class
title: SFC Seasonally flooded cropland (Nakas)
system: registry:L31
code: SFC
name: Seasonally flooded cropland (Nakas)
status: registered
decomposed: true
file_class_id: '10'
n_rows: 25
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L31
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L31/L31.lccs
schema: okf/0.1
---

# SFC Seasonally flooded cropland (Nakas)

## Definition (verbatim, FAO LCLR)

Farmland located parallel or close to the river, cultivated after flooding, mainly with vegetables. Small parcels (from 30 sqm to 50 sqm) aggregated in larger patterns.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 11 | 12 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Postflooding]/description=Describe the postflooding, elements/LC_Characteristic[LC_Postflooding]/name=Postflooding, elements/LC_Characteristic[LC_FieldDistribution]/description=Describe the field distribution) |

Full rows: `../elements.csv`, class_id `10`.
