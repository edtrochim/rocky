---
id: registry:L15:SEEA-9
kind: class
title: SEEA 9 Shrubs and/or herbaceous vegetation, aquatic or regularly flooded
system: registry:L15
code: SEEA 9
name: Shrubs and/or herbaceous vegetation, aquatic or regularly flooded
status: registered
decomposed: true
file_class_id: 3F
n_rows: 60
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WaterBody
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L15
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L15/L15.lccs
schema: okf/0.1
---

# SEEA 9 Shrubs and/or herbaceous vegetation, aquatic or regularly flooded

## Definition (verbatim, FAO LCLR)

The category is composed of natural shrubs or herbs with a cover from 10 to 100 percent in aquatic or regularly flooded areas with water persistence from 2 to 12 months per year.

## Description

This class includes any geographical area dominated by natural herbaceous vegetation (cover of 10 per cent or more) that is permanently or regularly flooded by fresh or rackish water (swamps, marsh areas, etc.). Flooding must persist for at least two months per year to be considered regular. Woody vegetation (trees and/or shrubs) can be present if their cover is less than 10 per cent.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 40 | 41 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 10.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 40 | 44 Optional | `LC_WoodyGrowthForm` | Mandatory | 1.0–9.0 |  | LC_VegetationArtificialityCharacteristic |
| 40 | 47 Mandatory | `LC_WaterBody` | Exclusive |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months | LC_WaterSalinityCharacteristic (type=Fresh) |
| 40 | 47 Mandatory | `LC_WaterBody` | Exclusive |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months | LC_WaterSalinityCharacteristic (type=Brackish) |

Full rows: `../elements.csv`, class_id `3F`.
