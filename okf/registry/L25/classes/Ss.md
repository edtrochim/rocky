---
id: registry:L25:Ss
kind: class
title: Ss Soil, sand deposit
system: registry:L25
code: Ss
name: Soil, sand deposit
status: registered
decomposed: true
file_class_id: 2B9
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_SoilSandDepositsSurfaceElement
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_SoilSandDepositsSurfaceElement
  path: ../../../vocab/elements/LC_SoilSandDepositsSurfaceElement.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Ss Soil, sand deposit

## Definition (verbatim, FAO LCLR)

It corresponds to areas with natural surfaces where the soil, sand and deposits are dominant. The presence of sub-surfaces is recognized with main physiognomic aspect.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2BA | 2BB Mandatory | `LC_SoilSandDepositsSurfaceElement` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `2B9`.
