---
id: registry:L35:HT
kind: class
title: HT Closed to open herbaceous vegetation with sparse trees and shrubs
system: registry:L35
code: HT
name: Closed to open herbaceous vegetation with sparse trees and shrubs
status: registered
decomposed: true
file_class_id: D9
n_rows: 42
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L35
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L35/L35.lccs
schema: okf/0.1
---

# HT Closed to open herbaceous vegetation with sparse trees and shrubs

## Definition (verbatim, FAO LCLR)

NA

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| DA | 172 Mandatory | `LC_Shrub` | Mandatory | 4.0–15.0 |  | LC_VegetationArtificialityCharacteristic |
| DA | 16F Mandatory | `LC_Tree` | Mandatory | 4.0–15.0 |  | LC_VegetationArtificialityCharacteristic |
| DA | F0 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 40.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `D9`.
