---
id: registry:L20:He_ein
kind: class
title: He_ein Consolidated rock
system: registry:L20
code: He_ein
name: Consolidated rock
status: registered
decomposed: true
file_class_id: F9
n_rows: 39
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L20
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L20/L20.lccs
schema: okf/0.1
---

# He_ein Consolidated rock

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| FA | FB Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 15.0–100.0 | height 0.0–150.0 |  |
| FA | FD Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/period_type=Atmospheric | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `F9`.
