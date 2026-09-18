---
id: registry:L15:SEEA-6
kind: class
title: SEEA 6 Trees covered areas
system: registry:L15
code: SEEA 6
name: Trees covered areas
status: registered
decomposed: true
file_class_id: '73'
n_rows: 59
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
- LC_WaterBody
links:
- rel: in_system
  id: registry:L15
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L15/L15.lccs
schema: okf/0.1
---

# SEEA 6 Trees covered areas

## Definition (verbatim, FAO LCLR)

The category is composed of a main layer of natural trees with a cover from 10 to 100 per cent.

## Description

This class includes any geographical area dominated by natural tree plants with a cover of 10 per cent or more. Other types of plants (shrubs and/or herbs) can be present, even with a density higher than that of trees. Areas planted with trees for afforestation purposes and forest plantations are included in this class. This class includes areas seasonally or permanently flooded with freshwater. It excludes coastal mangroves (→07).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 74 | 75 Mandatory | `LC_Tree` | Mandatory | 10.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 74 | 78 Optional | `LC_Shrub` | Mandatory | 1.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 74 | 7A Optional | `LC_HerbaceousGrowthForm` | Mandatory | 1.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 74 | 7C Optional | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months | LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `73`.
