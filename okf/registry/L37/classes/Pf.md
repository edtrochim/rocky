---
id: registry:L37:Pf
kind: class
title: Pf Forest plantation
system: registry:L37
code: Pf
name: Forest plantation
status: registered
decomposed: true
file_class_id: '22'
n_rows: 20
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L37
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L37/L37.LChS
schema: okf/0.1
---

# Pf Forest plantation

## Definition (verbatim, FAO LCLR)

This type of occupation refers to any form of vegetation made of trees planted by man for various needs (wood production, restoration and protection of soil). Generally isolated in highly humanized spaces, it appears on the image as a spot with sometimes a geometric shape. However, confusion is possible with sacred groves or other natural formations.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 23 | 24 Mandatory | `LC_Tree` | Mandatory |  | LC_WoodyGrowthLeafPhenology NaN–NaN | LC_CultivatedAndManagedVegetationCharacteristics;  (treePlantation=Forest Plantation); LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `22`.
