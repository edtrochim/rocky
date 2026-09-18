---
id: registry:L8:RB
kind: class
title: RB River banks
system: registry:L8
code: RB
name: River banks
status: registered
decomposed: true
file_class_id: D8
n_rows: 33
rows_in: ../elements.csv
element_refs:
- LC_LooseAndShiftingSand
- LC_WaterBody
links:
- rel: in_system
  id: registry:L8
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_LooseAndShiftingSand
  path: ../../../vocab/elements/LC_LooseAndShiftingSand.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L8/L8.lccs
schema: okf/0.1
---

# RB River banks

## Definition (verbatim, FAO LCLR)

The river bank is the natural land alongside the bed of a river which is usually consists of soil and sand deposits and inundated when water course flows with full capacity.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| D9 | 297 Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/period_type=Seasonal |  |
| D9 | DA Mandatory | `LC_LooseAndShiftingSand` | Mandatory |  |  | LC_NaturalSurfaceCharacteristic |

Full rows: `../elements.csv`, class_id `D8`.
