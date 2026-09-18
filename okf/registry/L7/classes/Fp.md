---
id: registry:L7:Fp
kind: class
title: Fp Fish ponds
system: registry:L7
code: Fp
name: Fish ponds
status: registered
decomposed: true
file_class_id: E6
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L7
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L7/L7.lccs
schema: okf/0.1
---

# Fp Fish ponds

## Definition (verbatim, FAO LCLR)

Human-constructed body of standing water with an area of variable size that is usually smaller than a lake.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| E7 | E8 Mandatory | `LC_WaterBody` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `E6`.
