---
id: registry:L25:Ad
kind: class
title: Ad Closed tree formation
system: registry:L25
code: Ad
name: Closed tree formation
status: registered
decomposed: true
file_class_id: 4C
n_rows: 40
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

# Ad Closed tree formation

## Definition (verbatim, FAO LCLR)

This class is very basic, and generic being constituted by one mandatory stratum that defines the overall class structure. The strata are constituted by one basic element tree. The element tree has two attributes i.e., (1) cover expressed in percent of plant covering the ground ranging from 70 - 100 % and (2) vegetation artificiality in this case is defined as natural vegetation.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4D | 51 Optional | `LC_Tree` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 4D | 54 Optional | `LC_Shrub` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 4D | 4E Mandatory | `LC_Tree` | Mandatory | 70.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `4C`.
