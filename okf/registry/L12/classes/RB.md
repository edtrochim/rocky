---
id: registry:L12:RB
kind: class
title: RB River bank
system: registry:L12
code: RB
name: River bank
status: registered
decomposed: true
file_class_id: '39'
n_rows: 37
rows_in: ../elements.csv
element_refs:
- LC_SoilSandDepositsSurfaceElement
- LC_WaterBody
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_SoilSandDepositsSurfaceElement
  path: ../../../vocab/elements/LC_SoilSandDepositsSurfaceElement.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# RB River bank

## Definition (verbatim, FAO LCLR)

River bank (soil / sand deposits) + perenial or periodic flowing fresh water (river), occasionally with loose scattered rocks, often with adjacent trees and shrubs.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3A | 3B Mandatory | `LC_SoilSandDepositsSurfaceElement` | Mandatory |  |  |  |
| 3A | 3D Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; dynamics=Flowing | LC_WaterSalinityCharacteristic (type=Fresh); LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `39`.
