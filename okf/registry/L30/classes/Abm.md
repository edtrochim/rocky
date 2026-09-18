---
id: registry:L30:Abm
kind: class
title: Abm Non tree shrub
system: registry:L30
code: Abm
name: Non tree shrub
status: registered
decomposed: true
file_class_id: 1D8
n_rows: 35
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L30
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L30/L30.lccs
schema: okf/0.1
---

# Abm Non tree shrub

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1DB | 1DC Mandatory | `LC_Shrub` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 1DB | 1DF Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `1D8`.
