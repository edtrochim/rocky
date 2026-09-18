---
id: registry:L26:WB
kind: class
title: WB Seasonal water bodies
system: registry:L26
code: WB
name: Seasonal water bodies
status: registered
decomposed: true
file_class_id: '23'
n_rows: 33
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_WaterBody
links:
- rel: in_system
  id: registry:L26
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L26/L26.lccs
schema: okf/0.1
---

# WB Seasonal water bodies

## Definition (verbatim, FAO LCLR)

Seasonal water bodies. Bare soil when water is not present.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 24 | 25 Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; dynamics=Standing | LC_WaterSalinityCharacteristic (type=Fresh) |
| 24 | 4B Mandatory | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `23`.
