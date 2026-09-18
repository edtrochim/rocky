---
id: registry:L8:MF
kind: class
title: MF Mud flats or inter tidal areas
system: registry:L8
code: MF
name: Mud flats or inter tidal areas
status: registered
decomposed: true
file_class_id: CF
n_rows: 43
rows_in: ../elements.csv
element_refs:
- LC_InorganicDeposits
- LC_WaterBody
links:
- rel: in_system
  id: registry:L8
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_InorganicDeposits
  path: ../../../vocab/elements/LC_InorganicDeposits.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L8/L8.lccs
schema: okf/0.1
---

# MF Mud flats or inter tidal areas

## Definition (verbatim, FAO LCLR)

Mud flats or intertidal areas are wet land soil near the estuary. It is submerged and exposed twice daily by tidal water.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 28F | 290 Mandatory | `LC_InorganicDeposits` | Mandatory |  | type=Silts and Clay |  |
| 28F | 292 Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Hours; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/period_type=Tidal | LC_WaterSalinityCharacteristic (type=Saline); LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `CF`.
