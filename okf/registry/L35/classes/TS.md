---
id: registry:L35:TS
kind: class
title: TS Closed to open temporarily flooded shrubs
system: registry:L35
code: TS
name: Closed to open temporarily flooded shrubs
status: registered
decomposed: true
file_class_id: D3
n_rows: 34
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_WaterBody
links:
- rel: in_system
  id: registry:L35
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L35/L35.lccs
schema: okf/0.1
---

# TS Closed to open temporarily flooded shrubs

## Definition (verbatim, FAO LCLR)

NA

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| D4 | 16B Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/period_type=Temporary |  |
| D4 | EA Mandatory | `LC_Shrub` | Mandatory | 40.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `D3`.
