---
id: registry:L21:Rp
kind: class
title: Rp Rubber plantation
system: registry:L21
code: Rp
name: Rubber plantation
status: registered
decomposed: true
file_class_id: '91'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L21
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L21/L21.lccs
schema: okf/0.1
---

# Rp Rubber plantation

## Definition (verbatim, FAO LCLR)

Areas currently supporting, and areas reserved for, rubber plantation.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 92 | 93 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_ForestPlantation]/name=Forest Plantation, elements/LC_Characteristic[LC_ForestPlantation]/description=Describe the forest plantation) |

Full rows: `../elements.csv`, class_id `91`.
