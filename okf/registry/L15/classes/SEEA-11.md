---
id: registry:L15:SEEA-11
kind: class
title: SEEA 11 Terrestrial barren land
system: registry:L15
code: SEEA 11
name: Terrestrial barren land
status: registered
decomposed: true
file_class_id: '57'
n_rows: 39
rows_in: ../elements.csv
element_refs:
- LC_GrowthForm
- LC_NaturalSurfaceElement
- LC_WaterBody
links:
- rel: in_system
  id: registry:L15
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_GrowthForm
  path: ../../../vocab/elements/LC_GrowthForm.md
- rel: uses_type
  id: element:LC_NaturalSurfaceElement
  path: ../../../vocab/elements/LC_NaturalSurfaceElement.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L15/L15.lccs
schema: okf/0.1
---

# SEEA 11 Terrestrial barren land

## Definition (verbatim, FAO LCLR)

The category is composed of abiotic natural surfaces.

## Description

This class includes any geographical area dominated by natural abiotic surfaces (bare soil, sand, rocks, etc.) where the natural vegetation is absent or almost absent (covers less than 2 per cent). The class includes areas regularly flooded by inland water (lake shores, river banks, salt flats, etc.). It excludes coastal areas affected by the tidal movement of saltwater (→14).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 58 | 59 Mandatory | `LC_NaturalSurfaceElement` | Mandatory |  |  |  |
| 58 | 5B Optional | `LC_GrowthForm` | Mandatory | 1.0–2.0 |  | LC_VegetationArtificialityCharacteristic |
| 58 | 5E Optional | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months |  |

Full rows: `../elements.csv`, class_id `57`.
