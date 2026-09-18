---
id: registry:L13:TP
kind: class
title: TP Tree Plantation
system: registry:L13
code: TP
name: Tree Plantation
status: registered
decomposed: true
file_class_id: '8'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L13
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L13/L13.lccs
schema: okf/0.1
---

# TP Tree Plantation

## Definition (verbatim, FAO LCLR)

Tree crops or planted trees.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 9 | A Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Plantation]/name=Plantation, elements/LC_Characteristic[LC_Plantation]/description=Describe the plantation) |

Full rows: `../elements.csv`, class_id `8`.
