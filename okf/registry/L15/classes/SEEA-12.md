---
id: registry:L15:SEEA-12
kind: class
title: SEEA 12 Permanent snow and glaciers
system: registry:L15
code: SEEA 12
name: Permanent snow and glaciers
status: registered
decomposed: true
file_class_id: '60'
n_rows: 36
rows_in: ../elements.csv
element_refs:
- LC_Ice
- LC_Snow
links:
- rel: in_system
  id: registry:L15
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Ice
  path: ../../../vocab/elements/LC_Ice.md
- rel: uses_type
  id: element:LC_Snow
  path: ../../../vocab/elements/LC_Snow.md
sources:
- okf/registry/_raw/L15/L15.lccs
schema: okf/0.1
---

# SEEA 12 Permanent snow and glaciers

## Definition (verbatim, FAO LCLR)

The category is composed of abiotic natural surfaces.

## Description

This class includes any geographical area covered by snow or glaciers persistently for 10 months or more.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 61 | 62 Mandatory | `LC_Snow` | Exclusive |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months | LC_ArtificialityCharacteristic (type=Natural) |
| 61 | 62 Mandatory | `LC_Ice` | Exclusive |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months | LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `60`.
