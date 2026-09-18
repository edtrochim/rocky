---
id: registry:L25:Cab
kind: class
title: Cab Shrub crop plantation
system: registry:L25
code: Cab
name: Shrub crop plantation
status: registered
decomposed: true
file_class_id: 1CA
n_rows: 31
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

# Cab Shrub crop plantation

## Definition (verbatim, FAO LCLR)

It corresponds to areas with cultivated rainfed agriculture where the growth form shrub is dominant.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1CB | 1CC Mandatory | `LC_Shrub` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed) |
| 1CB | 1D0 Optional | `LC_Tree` | Mandatory | 5.0–20.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `1CA`.
