---
id: registry:L4:FP
kind: class
title: FP Forest plantation
system: registry:L4
code: FP
name: Forest plantation
status: registered
decomposed: true
file_class_id: '26'
n_rows: 21
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L4
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L4/L4.lccs
schema: okf/0.1
---

# FP Forest plantation

## Definition (verbatim, FAO LCLR)

Cultivated and managed forest plantation.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 27 | 28 Mandatory | `LC_Tree` | Mandatory | 60.0–100.0 | height 0.0–0.0 | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_ForestPlantation]/name=Forest Plantation, elements/LC_Characteristic[LC_ForestPlantation]/description=Describe the forest plantation) |

Full rows: `../elements.csv`, class_id `26`.
