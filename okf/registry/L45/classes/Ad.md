---
id: registry:L45:Ad
kind: class
title: Ad Closed forest
system: registry:L45
code: Ad
name: Closed forest
status: registered
decomposed: true
file_class_id: '3'
n_rows: 40
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L45
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L45/L45.lccs
schema: okf/0.1
---

# Ad Closed forest

## Definition (verbatim, FAO LCLR)

Lands dominated by trees with a percent cover >70% during the entire year.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4 | 5 Optional | `LC_Shrub` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 4 | 8 Optional | `LC_Tree` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 4 | B Mandatory | `LC_Tree` | Mandatory | 70.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `3`.
