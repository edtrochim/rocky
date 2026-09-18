---
id: registry:L3:IA
kind: class
title: IA Industrial Area
system: registry:L3
code: IA
name: Industrial Area
status: registered
decomposed: true
file_class_id: '163'
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_OtherConstruction
links:
- rel: in_system
  id: registry:L3
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_OtherConstruction
  path: ../../../vocab/elements/LC_OtherConstruction.md
sources:
- okf/registry/_raw/L3/L3.lccs
schema: okf/0.1
---

# IA Industrial Area

## Definition (verbatim, FAO LCLR)

Non-urban build-up areas and other constructions (industrial etc...)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 164 | 165 Mandatory | `LC_OtherConstruction` | Mandatory |  |  | LC_ConstructionUse (type=Industrial area) |

Full rows: `../elements.csv`, class_id `163`.
