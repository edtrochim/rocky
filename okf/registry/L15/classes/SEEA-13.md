---
id: registry:L15:SEEA-13
kind: class
title: SEEA 13 Inland water bodies
system: registry:L15
code: SEEA 13
name: Inland water bodies
status: registered
decomposed: true
file_class_id: '67'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L15
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L15/L15.lccs
schema: okf/0.1
---

# SEEA 13 Inland water bodies

## Definition (verbatim, FAO LCLR)

The category is composed of any type of inland water body with a water persistence of 12 months per year.

## Description

This class includes any geographical area covered for most of the year by inland water bodies. In some cases, the water can be frozen for part of the year (less than 10 months). Because the geographical extent of water bodies can change, boundaries must be set consistently with those set by class 11, according to the dominant situation during the year and/or across multiple years.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 68 | 69 Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months |  |

Full rows: `../elements.csv`, class_id `67`.
