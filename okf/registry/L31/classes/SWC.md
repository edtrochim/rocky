---
id: registry:L31:SWC
kind: class
title: SWC Seasonal water channel
system: registry:L31
code: SWC
name: Seasonal water channel
status: registered
decomposed: true
file_class_id: A3
n_rows: 20
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L31
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L31/L31.lccs
schema: okf/0.1
---

# SWC Seasonal water channel

## Definition (verbatim, FAO LCLR)

Water channels that occur at some time of the year (rain season)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| A4 | A5 Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; dynamics=Flowing |  |

Full rows: `../elements.csv`, class_id `A3`.
