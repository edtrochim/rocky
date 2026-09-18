---
id: registry:L11:IA
kind: class
title: IA Industrial area
system: registry:L11
code: IA
name: Industrial area
status: registered
decomposed: true
file_class_id: E9
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_OtherConstruction
links:
- rel: in_system
  id: registry:L11
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_OtherConstruction
  path: ../../../vocab/elements/LC_OtherConstruction.md
sources:
- okf/registry/_raw/L11/L11.lccs
schema: okf/0.1
---

# IA Industrial area

## Definition (verbatim, FAO LCLR)

Non urban built up areas and other constructions (industrial, airport, etc).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| EA | EB Mandatory | `LC_OtherConstruction` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `E9`.
