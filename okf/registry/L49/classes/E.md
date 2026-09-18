---
id: registry:L49:E
kind: class
title: E Water
system: registry:L49
code: E
name: Water
status: registered
decomposed: true
file_class_id: '17'
n_rows: 35
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L49
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L49/L49.LChS
schema: okf/0.1
---

# E Water

## Definition (verbatim, FAO LCLR)

This class represents all types of water including, streams, rivers, lakes, ponds, reservoirs and oceans. (FAO, 2020). It is expressed as follows: •Single stratum of water body. •

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 17 | 27 Fixed | `LC_WaterBody` | Fixed | 0–100 | depth -100–0; persistencePeriod 0–365; density 0–999; lengthOfTemporalRelationship 1–100 |  |

Full rows: `../elements.csv`, class_id `17`.
