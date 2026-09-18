---
id: registry:L15:SEEA-14
kind: class
title: SEEA 14 Coastal water bodies and intertidal areas
system: registry:L15
code: SEEA 14
name: Coastal water bodies and intertidal areas
status: registered
decomposed: true
file_class_id: 6C
n_rows: 37
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

# SEEA 14 Coastal water bodies and intertidal areas

## Definition (verbatim, FAO LCLR)

The category is composed on the basis of geographical features in relation to the sea (lagoons and estuaries) and abiotic surfaces subject to water persistence (intertidal variations).

## Description

The class is defined on the basis of geographical features of the land in relation to the sea (coastal water bodies, i.e., lagoons and estuaries) and abiotic surfaces subject to water persistence (intertidal areas, i.e., coastal flats and coral reefs).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 6E | 6F Mandatory | `LC_WaterBody` | Exclusive |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months |  |
| 6E | 6F Mandatory | `LC_WaterBody` | Exclusive |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_period 6.0–12.0; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/period_type=Tidal | LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `6C`.
