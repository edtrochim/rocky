---
id: registry:L30:Ch
kind: class
title: Ch Chott
system: registry:L30
code: Ch
name: Chott
status: registered
decomposed: true
file_class_id: FC
n_rows: 37
rows_in: ../elements.csv
element_refs:
- LC_InorganicDeposits
- LC_WaterBody
links:
- rel: in_system
  id: registry:L30
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_InorganicDeposits
  path: ../../../vocab/elements/LC_InorganicDeposits.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L30/L30.lccs
schema: okf/0.1
---

# Ch Chott

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| FD | 100 Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Hours; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_period 1.0–1.0 | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Saline) |
| FD | FE Mandatory | `LC_InorganicDeposits` | Mandatory |  | type=Salt Flat |  |

Full rows: `../elements.csv`, class_id `FC`.
