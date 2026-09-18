---
id: registry:L30:Sbl
kind: class
title: Sbl Sebkha coastline
system: registry:L30
code: Sbl
name: Sebkha coastline
status: registered
decomposed: true
file_class_id: F1
n_rows: 48
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_InorganicDeposits
- LC_LooseAndShiftingSand
- LC_WaterBody
links:
- rel: in_system
  id: registry:L30
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_InorganicDeposits
  path: ../../../vocab/elements/LC_InorganicDeposits.md
- rel: uses_type
  id: element:LC_LooseAndShiftingSand
  path: ../../../vocab/elements/LC_LooseAndShiftingSand.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L30/L30.lccs
schema: okf/0.1
---

# Sbl Sebkha coastline

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| F3 | F4 Mandatory | `LC_InorganicDeposits` | Exclusive |  | type=Salt Flat |  |
| F3 | F4 Mandatory | `LC_BareSoil` | Exclusive |  |  |  |
| F3 | F4 Mandatory | `LC_LooseAndShiftingSand` | Exclusive |  |  |  |
| F3 | F8 Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; dynamics=Standing | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Brackish) |

Full rows: `../elements.csv`, class_id `F1`.
