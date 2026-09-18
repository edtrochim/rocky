---
id: registry:L42:Gh
kind: class
title: Gh Greenhouse
system: registry:L42
code: Gh
name: Greenhouse
status: registered
decomposed: true
file_class_id: 6E
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_OtherConstruction
links:
- rel: in_system
  id: registry:L42
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_OtherConstruction
  path: ../../../vocab/elements/LC_OtherConstruction.md
sources:
- okf/registry/_raw/L42/L42.lccs
schema: okf/0.1
---

# Gh Greenhouse

## Definition (verbatim, FAO LCLR)

Crops under cover are crops under greenhouses, in protected area of agriculture.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 6F | 70 Mandatory | `LC_OtherConstruction` | Mandatory |  |  | LC_ConstructionUse (type=Greenhouse) |

Full rows: `../elements.csv`, class_id `6E`.
