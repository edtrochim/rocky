---
id: registry:L28:Wi
kind: class
title: Wi Inland water
system: registry:L28
code: Wi
name: Inland water
status: registered
decomposed: true
file_class_id: 9E
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L28
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L28/L28.lccs
schema: okf/0.1
---

# Wi Inland water

## Definition (verbatim, FAO LCLR)

Inland water bodies generally include major rivers, lakes and water reservoirs.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 9F | A0 Mandatory | `LC_WaterBody` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `9E`.
