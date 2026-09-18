---
id: registry:L13:WN
kind: class
title: WN Natural Waterbodies
system: registry:L13
code: WN
name: Natural Waterbodies
status: registered
decomposed: true
file_class_id: '79'
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L13
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L13/L13.lccs
schema: okf/0.1
---

# WN Natural Waterbodies

## Definition (verbatim, FAO LCLR)

Natural body of water including rivers, ocean, spring, stream, pond, lake, or wetland that was historically present in a natural state but may have been physically altered over time.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 7A | 7B Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `79`.
