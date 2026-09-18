---
id: registry:L15:SEEA-8
kind: class
title: SEEA 8 Shrub covered areas
system: registry:L15
code: SEEA 8
name: Shrub covered areas
status: registered
decomposed: true
file_class_id: '31'
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

# SEEA 8 Shrub covered areas

## Definition (verbatim, FAO LCLR)

The category is composed of a main layer of natural shrubs with a cover from 10 to 100 per cent.

## Description

This class includes any geographical area dominated by natural shrubs having a cover of 10 per cent or more. Trees can be present in scattered form if their cover is less than 10 per cent. Herbaceous plants can also be present at any density. The class includes shrub-covered areas permanently or regularly flooded by inland fresh water. It excludes shrubs flooded by salt or brackish water in coastal areas (→07).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 32 | 33 Mandatory | `LC_Shrub` | Mandatory | 10.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 32 | 36 Optional | `LC_Tree` | Mandatory | 1.0–9.0 |  | LC_VegetationArtificialityCharacteristic |
| 32 | 39 Optional | `LC_HerbaceousGrowthForm` | Mandatory | 1.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 32 | 3C Optional | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months | LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `31`.
