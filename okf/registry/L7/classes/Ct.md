---
id: registry:L7:Ct
kind: class
title: Ct Closed Tree Dominated
system: registry:L7
code: Ct
name: Closed Tree Dominated
status: registered
decomposed: true
file_class_id: '2'
n_rows: 40
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L7
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L7/L7.lccs
schema: okf/0.1
---

# Ct Closed Tree Dominated

## Definition (verbatim, FAO LCLR)

Closed (>80%) undifferentiated trees, sometimes mixed broadleaved and needle-leaved; occasionally with shrubs.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3 | 4 Mandatory | `LC_Tree` | Mandatory | 80.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 3 | 7 Optional | `LC_Tree` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 3 | A Optional | `LC_Shrub` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `2`.
