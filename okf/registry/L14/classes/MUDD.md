---
id: registry:L14:MUDD
kind: class
title: MUDD Dry mudflat
system: registry:L14
code: MUDD
name: Dry mudflat
status: registered
decomposed: true
file_class_id: B1
n_rows: 39
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_WaterBody
links:
- rel: in_system
  id: registry:L14
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L14/L14.lccs
schema: okf/0.1
---

# MUDD Dry mudflat

## Definition (verbatim, FAO LCLR)

Mud deposits regularly flooded by stream. Flooding persists 1-2 months

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| B3 | B4 Mandatory | `LC_BareSoil` | Mandatory |  |  |  |
| B3 | B6 Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_period 1.0–2.0 | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `B1`.
