---
id: registry:L29:lcc6
kind: class
title: lcc6 Glacier
system: registry:L29
code: lcc6
name: Glacier
status: registered
decomposed: true
file_class_id: 4B
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_Ice
- LC_LooseAndShiftingSand
- LC_Snow
links:
- rel: in_system
  id: registry:L29
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Ice
  path: ../../../vocab/elements/LC_Ice.md
- rel: uses_type
  id: element:LC_LooseAndShiftingSand
  path: ../../../vocab/elements/LC_LooseAndShiftingSand.md
- rel: uses_type
  id: element:LC_Snow
  path: ../../../vocab/elements/LC_Snow.md
sources:
- okf/registry/_raw/L29/L29.lccs
schema: okf/0.1
---

# lcc6 Glacier

## Definition (verbatim, FAO LCLR)

Perennial ice in movement.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4C | 4D Mandatory | `LC_Snow` | Mandatory |  |  |  |
| 4C | 4D Mandatory | `LC_Ice` | Optional |  |  |  |
| 4C | 4D Mandatory | `LC_LooseAndShiftingSand` | Optional |  |  |  |

Full rows: `../elements.csv`, class_id `4B`.
