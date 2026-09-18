---
id: registry:L20:Mn_p
kind: class
title: Mn_p Native park forest
system: registry:L20
code: Mn_p
name: Native park forest
status: registered
decomposed: true
file_class_id: '41'
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_Graminoid
- LC_Tree
links:
- rel: in_system
  id: registry:L20
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Graminoid
  path: ../../../vocab/elements/LC_Graminoid.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L20/L20.lccs
schema: okf/0.1
---

# Mn_p Native park forest

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 42 | 43 Mandatory | `LC_Tree` | Mandatory | 15.0–40.0 |  | LC_VegetationArtificialityCharacteristic |
| 42 | 46 Mandatory | `LC_Graminoid` | Mandatory | 80.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `41`.
