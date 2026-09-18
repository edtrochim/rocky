---
id: registry:L8:BH
kind: class
title: BH Perennial beels/haors
system: registry:L8
code: BH
name: Perennial beels/haors
status: registered
decomposed: true
file_class_id: FA
n_rows: 27
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L8
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L8/L8.lccs
schema: okf/0.1
---

# BH Perennial beels/haors

## Definition (verbatim, FAO LCLR)

Natural water reservoir, billabong or a lake-like wetland with static water. It becomes very extensive water body in the monsoon and dries up mostly in the post-monsoon period.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| FB | FC Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Standing; position=Above Surface | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `FA`.
