---
id: registry:L41:Rmo
kind: class
title: Rmo Orchards
system: registry:L41
code: Rmo
name: Orchards
status: registered
decomposed: true
file_class_id: '65'
n_rows: 23
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L41
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L41/L41.lccs
schema: okf/0.1
---

# Rmo Orchards

## Definition (verbatim, FAO LCLR)

Cultivated agricultural areas with fruit-bearing trees typically in rainfed systems.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 66 | 67 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_Plantation]/name=Plantation) |

Full rows: `../elements.csv`, class_id `65`.
