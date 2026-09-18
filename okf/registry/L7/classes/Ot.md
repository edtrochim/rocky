---
id: registry:L7:Ot
kind: class
title: Ot Open Tree Dominated
system: registry:L7
code: Ot
name: Open Tree Dominated
status: registered
decomposed: true
file_class_id: E
n_rows: 29
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

# Ot Open Tree Dominated

## Definition (verbatim, FAO LCLR)

Open (20-80%) undifferentiated trees, sometimes mixed broadleaved and needle-leaved; occasionally with shrubs.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| F | 10 Mandatory | `LC_Tree` | Mandatory | 20.0–80.0 |  | LC_VegetationArtificialityCharacteristic |
| F | 13 Optional | `LC_Shrub` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `E`.
