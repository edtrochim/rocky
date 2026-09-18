---
id: registry:L25:Abis
kind: class
title: Abis Seasonally flooded shrubs
system: registry:L25
code: Abis
name: Seasonally flooded shrubs
status: registered
decomposed: true
file_class_id: 15E
n_rows: 35
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_WaterBody
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Abis Seasonally flooded shrubs

## Definition (verbatim, FAO LCLR)

This class describes the generic aspects of the class referred to as the seasonally flooded shrubs. The strata are constituted by two basic elements: shrubs and water body.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 15F | 160 Mandatory | `LC_Shrub` | Mandatory | 20.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 15F | 163 Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months | LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `15E`.
