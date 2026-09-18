---
id: registry:L7:Rhc
kind: class
title: Rhc Herbaceous Crops
system: registry:L7
code: Rhc
name: Herbaceous Crops
status: registered
decomposed: true
file_class_id: '70'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L7
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L7/L7.lccs
schema: okf/0.1
---

# Rhc Herbaceous Crops

## Definition (verbatim, FAO LCLR)

Lands covered with temporary rainfed herbaceous crops followed by harvest and a bare soil period.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 71 | 72 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed) |

Full rows: `../elements.csv`, class_id `70`.
