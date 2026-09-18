---
id: registry:L51:Wa
kind: class
title: Wa Water​
system: registry:L51
code: Wa
name: Water​
status: registered
decomposed: true
file_class_id: '10'
n_rows: 35
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L51
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L51/L51.LChS
schema: okf/0.1
---

# Wa Water​

## Definition (verbatim, FAO LCLR)

Permanent or seasonally flooded surfaces covered by inland or coastal water bodies (e.g. rivers, lakes, reservoirs, ponds).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 10 | 15 Fixed | `LC_WaterBody` | Fixed | 0–100 | depth -100–0; persistencePeriod 0–365; density 0–999; lengthOfTemporalRelationship 1–100 |  |

Full rows: `../elements.csv`, class_id `10`.
