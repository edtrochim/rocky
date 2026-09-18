---
id: registry:L7:Rscp
kind: class
title: Rscp Shrub Crop
system: registry:L7
code: Rscp
name: Shrub Crop
status: registered
decomposed: true
file_class_id: 5C
n_rows: 31
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L7
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L7/L7.lccs
schema: okf/0.1
---

# Rscp Shrub Crop

## Definition (verbatim, FAO LCLR)

Cultivated agriculture with rainfed area where the growth form shrub is dominant.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 5D | 62 Optional | `LC_Tree` | Mandatory | 5.0–20.0 |  | LC_VegetationArtificialityCharacteristic |
| 5D | 5E Mandatory | `LC_Shrub` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed) |

Full rows: `../elements.csv`, class_id `5C`.
