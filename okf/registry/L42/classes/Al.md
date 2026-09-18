---
id: registry:L42:Al
kind: class
title: Al Artificial land
system: registry:L42
code: Al
name: Artificial land
status: registered
decomposed: true
file_class_id: 2A
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_NonLinearSurface
links:
- rel: in_system
  id: registry:L42
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_NonLinearSurface
  path: ../../../vocab/elements/LC_NonLinearSurface.md
sources:
- okf/registry/_raw/L42/L42.lccs
schema: okf/0.1
---

# Al Artificial land

## Definition (verbatim, FAO LCLR)

Artificial land includes urbanized areas, activity zones, non-built artificial areas, and non-agricultural artificial green spaces.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2B | 2C Mandatory | `LC_NonLinearSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `2A`.
