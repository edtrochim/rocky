---
id: registry:L45:Ac
kind: class
title: Ac Open forest
system: registry:L45
code: Ac
name: Open forest
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

# Ac Open forest

## Definition (verbatim, FAO LCLR)

Lands dominated by trees with a percent cover between 20 and 70% during the entire year.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| F | 10 Optional | `LC_Shrub` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| F | 13 Mandatory | `LC_Tree` | Mandatory | 20.0–70.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `E`.
