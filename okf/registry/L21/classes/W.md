---
id: registry:L21:W
kind: class
title: W Water
system: registry:L21
code: W
name: Water
status: registered
decomposed: true
file_class_id: 6A
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_WaterBodyAndAssociatedSurfaceElement
links:
- rel: in_system
  id: registry:L21
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBodyAndAssociatedSurfaceElement
  path: ../../../vocab/elements/LC_WaterBodyAndAssociatedSurfaceElement.md
sources:
- okf/registry/_raw/L21/L21.lccs
schema: okf/0.1
---

# W Water

## Definition (verbatim, FAO LCLR)

Area of fresh and sea water.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 6B | 6C Mandatory | `LC_WaterBodyAndAssociatedSurfaceElement` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `6A`.
