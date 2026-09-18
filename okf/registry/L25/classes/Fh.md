---
id: registry:L25:Fh
kind: class
title: Fh Moist forest
system: registry:L25
code: Fh
name: Moist forest
status: registered
decomposed: true
file_class_id: '57'
n_rows: 44
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

# Fh Moist forest

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of a so-called moist forest. It is constituted by one mandatory stratum that defines the overall class structure. The strata is constituted by one basic element tree.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 58 | 59 Mandatory | `LC_Tree` | Mandatory | 10.0–25.0 | height 25.0–50.0 | LC_VegetationArtificialityCharacteristic |
| 58 | 5C Mandatory | `LC_Tree` | Mandatory | 70.0–100.0 | height 8.0–25.0 | LC_VegetationArtificialityCharacteristic |
| 58 | 5F Mandatory | `LC_Shrub` | Mandatory | 10.0–60.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `57`.
