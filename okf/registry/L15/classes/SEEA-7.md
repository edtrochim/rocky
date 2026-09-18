---
id: registry:L15:SEEA-7
kind: class
title: SEEA 7 Mangroves
system: registry:L15
code: SEEA 7
name: Mangroves
status: registered
decomposed: true
file_class_id: '28'
n_rows: 49
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L15
  path: ../SYSTEM.md
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

# SEEA 7 Mangroves

## Definition (verbatim, FAO LCLR)

The category is composed of natural trees with a cover from 10 to 100 per cent in aquatic or regularly flooded areas in salt and brackish water.

## Description

This class includes any geographical area dominated by woody vegetation (trees and/or shrubs) with a cover of 10 per cent or more that is permanently or regularly flooded by salt and/or brackish water located in the coastal areas or in the deltas of rivers.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2A | 2B Mandatory | `LC_WoodyGrowthForm` | Mandatory | 10.0–100.0 | LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/name=Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/description=Contains the elements of Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Broadleaved]/name=Broadleaved; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Broadleaved]/description=Describe a Broadleaved type element; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Broadleaved]/percentage 100.0–100.0; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology | LC_VegetationArtificialityCharacteristic |
| 2A | 2E Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_period 6.0–24.0; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Hours | LC_WaterSalinityCharacteristic (type=Brackish) |

Full rows: `../elements.csv`, class_id `28`.
