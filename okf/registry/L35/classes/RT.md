---
id: registry:L35:RT
kind: class
title: RT Rainfed tree plantation(s)
system: registry:L35
code: RT
name: Rainfed tree plantation(s)
status: registered
decomposed: true
file_class_id: 1B
n_rows: 21
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L35
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L35/L35.lccs
schema: okf/0.1
---

# RT Rainfed tree plantation(s)

## Definition (verbatim, FAO LCLR)

NA

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1C | 1D Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Plantation]/name=Plantation, elements/LC_Characteristic[LC_Plantation]/description=Describe the plantation, elements/LC_Characteristic[LC_Rainfed]/name=Rainfed) |

Full rows: `../elements.csv`, class_id `1B`.
