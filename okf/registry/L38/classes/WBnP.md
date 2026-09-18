---
id: registry:L38:WBnP
kind: class
title: WBnP Water body seasonal
system: registry:L38
code: WBnP
name: Water body seasonal
status: registered
decomposed: true
file_class_id: '187'
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_WaterBodyAndAssociatedSurfaceElement
links:
- rel: in_system
  id: registry:L38
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBodyAndAssociatedSurfaceElement
  path: ../../../vocab/elements/LC_WaterBodyAndAssociatedSurfaceElement.md
sources:
- okf/registry/_raw/L38/L38.lccs
schema: okf/0.1
---

# WBnP Water body seasonal

## Definition (verbatim, FAO LCLR)

Natural fresh waterbody with oscillations in water level with perennial closed/open natural herbaceous vegetation

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 189 | 18A Mandatory | `LC_WaterBodyAndAssociatedSurfaceElement` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/period_type=Atmospheric | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `187`.
