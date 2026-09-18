---
id: registry:L15:SEEA-3
kind: class
title: SEEA 3 Woody crops
system: registry:L15
code: SEEA 3
name: Woody crops
status: registered
decomposed: true
file_class_id: '10'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L15
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L15/L15.lccs
schema: okf/0.1
---

# SEEA 3 Woody crops

## Definition (verbatim, FAO LCLR)

The category is composed of a main layer of cultivated tree or shrub plants.

## Description

The class is composed of a main layer of permanent crops (trees or shrub crops) and includes all types of orchards and plantations (fruit trees, coffee and tea plantation, oil palms, rubber plantation, Christmas trees, etc.).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 11 | 12 Mandatory | `LC_WoodyGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation) |

Full rows: `../elements.csv`, class_id `10`.
