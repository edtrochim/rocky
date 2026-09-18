---
id: registry:L15:SEEA-10
kind: class
title: SEEA 10 Sparsely natural vegetated areas
system: registry:L15
code: SEEA 10
name: Sparsely natural vegetated areas
status: registered
decomposed: true
file_class_id: '50'
n_rows: 31
rows_in: ../elements.csv
element_refs:
- LC_GrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L15
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_GrowthForm
  path: ../../../vocab/elements/LC_GrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L15/L15.lccs
schema: okf/0.1
---

# SEEA 10 Sparsely natural vegetated areas

## Definition (verbatim, FAO LCLR)

The category is composed of any type of natural vegetation (all growth forms) with a cover from 2 to 10 per cent.

## Description

This class includes any geographical areas were the cover of natural vegetation is between 2 per cent and 10 per cent. This includes permanently or regularly flooded areas.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 51 | 52 Mandatory | `LC_GrowthForm` | Mandatory | 2.0–9.0 |  | LC_VegetationArtificialityCharacteristic |
| 51 | 55 Optional | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months |  |

Full rows: `../elements.csv`, class_id `50`.
