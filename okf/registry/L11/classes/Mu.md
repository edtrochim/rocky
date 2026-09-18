---
id: registry:L11:Mu
kind: class
title: Mu Mudflat
system: registry:L11
code: Mu
name: Mudflat
status: registered
decomposed: true
file_class_id: A8
n_rows: 38
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_WaterBody
links:
- rel: in_system
  id: registry:L11
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L11/L11.lccs
schema: okf/0.1
---

# Mu Mudflat

## Definition (verbatim, FAO LCLR)

Unvegetated mud/sand deposits regularly flooded, between high and low water marks.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| AA | AB Mandatory | `LC_BareSoil` | Mandatory |  |  |  |
| AA | AD Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Saline) |

Full rows: `../elements.csv`, class_id `A8`.
