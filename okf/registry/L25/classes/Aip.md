---
id: registry:L25:Aip
kind: class
title: Aip Permanently flooded trees
system: registry:L25
code: Aip
name: Permanently flooded trees
status: registered
decomposed: true
file_class_id: 13E
n_rows: 35
rows_in: ../elements.csv
element_refs:
- LC_Tree
- LC_WaterBody
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Aip Permanently flooded trees

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of permanently flooded trees. It is constituted by two mandatory stratum that defines the overall class structure. The strata are constituted by two basic elements trees and water body.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 13F | 140 Mandatory | `LC_Tree` | Mandatory | 20.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 13F | 143 Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months | LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `13E`.
