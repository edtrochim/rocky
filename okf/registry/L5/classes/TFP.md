---
id: registry:L5:TFP
kind: class
title: TFP Tree forest plantations
system: registry:L5
code: TFP
name: Tree forest plantations
status: registered
decomposed: true
file_class_id: '71'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L5
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L5/L5.lccs
schema: okf/0.1
---

# TFP Tree forest plantations

## Definition (verbatim, FAO LCLR)

Tree forest plantation refers to governmental plantation. This class can be identified with large area and regular shape.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 72 | 73 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_ForestPlantation]/name=Forest Plantation, elements/LC_Characteristic[LC_ForestPlantation]/description=Describe the forest plantation) |

Full rows: `../elements.csv`, class_id `71`.
