---
id: registry:L14:IA
kind: class
title: IA Industrial and/or other areas
system: registry:L14
code: IA
name: Industrial and/or other areas
status: registered
decomposed: true
file_class_id: E9
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_OtherConstruction
links:
- rel: in_system
  id: registry:L14
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_OtherConstruction
  path: ../../../vocab/elements/LC_OtherConstruction.md
sources:
- okf/registry/_raw/L14/L14.lccs
schema: okf/0.1
---

# IA Industrial and/or other areas

## Definition (verbatim, FAO LCLR)

Non urban built up areas and other construictions (industrial, airport, etc)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| EA | EB Mandatory | `LC_OtherConstruction` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `E9`.
