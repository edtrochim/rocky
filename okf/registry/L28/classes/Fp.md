---
id: registry:L28:Fp
kind: class
title: Fp Forest plantation
system: registry:L28
code: Fp
name: Forest plantation
status: registered
decomposed: true
file_class_id: 1E
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L28
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L28/L28.lccs
schema: okf/0.1
---

# Fp Forest plantation

## Definition (verbatim, FAO LCLR)

Cultivation of trees.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1F | 20 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_ForestPlantation]/name=Forest Plantation, elements/LC_Characteristic[LC_ForestPlantation]/description=Describe the forest plantation) |

Full rows: `../elements.csv`, class_id `1E`.
