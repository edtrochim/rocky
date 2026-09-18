---
id: registry:L5:ROA
kind: class
title: ROA Roads
system: registry:L5
code: ROA
name: Roads
status: registered
decomposed: true
file_class_id: '42'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_LinearSurface
links:
- rel: in_system
  id: registry:L5
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_LinearSurface
  path: ../../../vocab/elements/LC_LinearSurface.md
sources:
- okf/registry/_raw/L5/L5.lccs
schema: okf/0.1
---

# ROA Roads

## Definition (verbatim, FAO LCLR)

Linear artificial structures, mainly major roads (motor-ways, primary roads).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 43 | 44 Mandatory | `LC_LinearSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `42`.
