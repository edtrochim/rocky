---
id: registry:L2:8WBS
kind: class
title: 8WBS Bare soil in seasonally flooded area
system: registry:L2
code: 8WBS
name: Bare soil in seasonally flooded area
status: registered
decomposed: true
file_class_id: FD
n_rows: 29
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_WaterBody
links:
- rel: in_system
  id: registry:L2
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L2/L2.lccs
schema: okf/0.1
---

# 8WBS Bare soil in seasonally flooded area

## Definition (verbatim, FAO LCLR)

Bare soil seasonally flooded (water presence: 1-3 months)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| FE | FF Mandatory | `LC_BareSoil` | Optional |  |  |  |
| FE | FF Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_period 1.0–9.0 | LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `FD`.
