---
id: registry:L15:SEEA-2
kind: class
title: SEEA 2 Herbaceous crops
system: registry:L15
code: SEEA 2
name: Herbaceous crops
status: registered
decomposed: true
file_class_id: B
n_rows: 17
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L15
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L15/L15.lccs
schema: okf/0.1
---

# SEEA 2 Herbaceous crops

## Definition (verbatim, FAO LCLR)

The category is composed of a main layer of cultivated herbaceous plants.

## Description

The class is composed of a main layer of cultivated herbaceous plants (graminoids or forbs). It includes herbaceous crops used for hay. All the non-perennial crops that do not last for more than two growing seasons and crops like sugar cane, where the upper part of the plant is regularly harvested while the root system can remain for more than one year in the field, are included in this class.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| C | D Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `B`.
