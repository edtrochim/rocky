---
id: registry:L12:HCP
kind: class
title: HCP Rainfed agriculture, plain areas
system: registry:L12
code: HCP
name: Rainfed agriculture, plain areas
status: registered
decomposed: true
file_class_id: BB
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# HCP Rainfed agriculture, plain areas

## Definition (verbatim, FAO LCLR)

Rainfed herbaceous crops cultivated in flat-lying plains (slope up to 10 degrees) relatively larger sized fields.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| BC | BD Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_FieldSize]/name=Field Size) |

Full rows: `../elements.csv`, class_id `BB`.
