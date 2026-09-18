---
id: registry:L29:lcc11
kind: class
title: lcc11 Riverbed
system: registry:L29
code: lcc11
name: Riverbed
status: registered
decomposed: true
file_class_id: 6D
n_rows: 31
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_WaterBody
links:
- rel: in_system
  id: registry:L29
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L29/L29.lccs
schema: okf/0.1
---

# lcc11 Riverbed

## Definition (verbatim, FAO LCLR)

A tract of land without vegetation surrounded by the waters of an ocean, lake, or stream; it usually includes any accretion in a river course.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 6E | 6F Mandatory | `LC_BareSoil` | Mandatory |  |  |  |
| 6E | 6F Mandatory | `LC_WaterBody` | Optional |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_period 10.0–20.0; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Years |  |

Full rows: `../elements.csv`, class_id `6D`.
