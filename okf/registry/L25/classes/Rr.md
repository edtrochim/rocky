---
id: registry:L25:Rr
kind: class
title: Rr River bank
system: registry:L25
code: Rr
name: River bank
status: registered
decomposed: true
file_class_id: 33C
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

# Rr River bank

## Definition (verbatim, FAO LCLR)

The riverbank is the land alongside the bed of a river which is usually consists of soil and sand deposits and inundated when the river flows with the fully capacity. This class describe the generic aspect of riverbank. It is constituted by two mandatory strata that defines the overall class structure. The strata is constituted by one basic element water body.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 33D | 340 Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Weeks; dynamics=Flowing | LC_WaterSalinityCharacteristic (type=Fresh); LC_ArtificialityCharacteristic (type=Natural) |
| 33D | 33E Mandatory | `LC_NaturalSurfaceElement` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `33C`.
