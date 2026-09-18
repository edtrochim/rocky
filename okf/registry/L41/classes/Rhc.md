---
id: registry:L41:Rhc
kind: class
title: Rhc Herbaceous Crops rainfed
system: registry:L41
code: Rhc
name: Herbaceous Crops rainfed
status: registered
decomposed: true
file_class_id: '70'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L41
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L41/L41.lccs
schema: okf/0.1
---

# Rhc Herbaceous Crops rainfed

## Definition (verbatim, FAO LCLR)

Areas covered with rainfed herbaceous growth forms, such as maize, wheat, barley, and sunflowers. These fields are typically small to medium-sized (1 Ha on average).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 71 | 72 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed) |

Full rows: `../elements.csv`, class_id `70`.
