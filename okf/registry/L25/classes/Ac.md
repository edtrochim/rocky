---
id: registry:L25:Ac
kind: class
title: Ac Open tree formation
system: registry:L25
code: Ac
name: Open tree formation
status: registered
decomposed: true
file_class_id: '69'
n_rows: 29
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Ac Open tree formation

## Definition (verbatim, FAO LCLR)

This class is very basic, and generic being constituted by one mandatory strata that defines the overall class aspect. The strata are constituted by one basic element tree. The element tree has two attributes i.e., (1) cover expressed in percent of plant covering the ground ranging from 20 - 70 % and (2) vegetation artificiality in this case is defined as natural.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 6A | 6B Mandatory | `LC_Tree` | Mandatory | 20.0–70.0 |  | LC_VegetationArtificialityCharacteristic |
| 6A | 6E Optional | `LC_Shrub` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `69`.
