---
id: registry:L26:WA
kind: class
title: WA Wadi and riverbed
system: registry:L26
code: WA
name: Wadi and riverbed
status: registered
decomposed: true
file_class_id: 3B
n_rows: 36
rows_in: ../elements.csv
element_refs:
- LC_NaturalSurfaceElement
- LC_WaterBody
links:
- rel: in_system
  id: registry:L26
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_NaturalSurfaceElement
  path: ../../../vocab/elements/LC_NaturalSurfaceElement.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L26/L26.lccs
schema: okf/0.1
---

# WA Wadi and riverbed

## Definition (verbatim, FAO LCLR)

Wadi and riverbed

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3C | B2 Mandatory | `LC_NaturalSurfaceElement` | Mandatory |  |  |  |
| 3C | B4 Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Hours; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/period_type=Atmospheric | LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `3B`.
