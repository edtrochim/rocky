---
id: registry:L25:W
kind: class
title: W Wadies
system: registry:L25
code: W
name: Wadies
status: registered
decomposed: true
file_class_id: '344'
n_rows: 36
rows_in: ../elements.csv
element_refs:
- LC_NaturalSurfaceElement
- LC_WaterBody
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_NaturalSurfaceElement
  path: ../../../vocab/elements/LC_NaturalSurfaceElement.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# W Wadies

## Definition (verbatim, FAO LCLR)

This class describe the generic aspect of Wadi. It is constituted by two mandatory strata that defines the overall class structure. The strata is constituted by one basic element water body.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 345 | 346 Mandatory | `LC_NaturalSurfaceElement` | Mandatory |  |  |  |
| 345 | 348 Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Weeks; dynamics=Flowing | LC_WaterSalinityCharacteristic (type=Fresh); LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `344`.
