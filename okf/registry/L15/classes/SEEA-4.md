---
id: registry:L15:SEEA-4
kind: class
title: SEEA 4 Multiple or layered crops
system: registry:L15
code: SEEA 4
name: Multiple or layered crops
status: registered
decomposed: true
file_class_id: '16'
n_rows: 35
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L15
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L15/L15.lccs
schema: okf/0.1
---

# SEEA 4 Multiple or layered crops

## Definition (verbatim, FAO LCLR)

The category is composed of at least two layers of cultivated woody and herbaceous plants or different layers of cultivated plants combined with natural vegetation.

## Description

This class combine two different land cover situations: 1. Two layers of different crops. A common case is the presence of one layer of woody crops (trees or shrubs) and another layer of herbaceous crop, e.g., wheat fields with olive trees in the Mediterranean area and intense horticulture, or oasis or typical coastal agriculture in Africa, where herbaceous fields are covered by palm trees. 2. Presence of one important layer of natural vegetation (mainly trees) that covers one layer of cultivated crops. Coffee plantations shadowed by natural trees in the equatorial area of Africa are a typical example.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 17 | 18 Mandatory | `LC_WoodyGrowthForm` | Exclusive |  |  | LC_CultivatedAndManagedVegetationCharacteristics |
| 17 | 18 Mandatory | `LC_WoodyGrowthForm` | Exclusive |  |  | LC_VegetationArtificialityCharacteristic |
| 17 | 1D Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `16`.
