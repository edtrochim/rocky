---
id: registry:L36:Abr
kind: class
title: Abr Marquis/garrigue
system: registry:L36
code: Abr
name: Marquis/garrigue
status: registered
decomposed: true
file_class_id: 16B
n_rows: 48
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L36
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
- okf/registry/_raw/L36/L36.lccs
schema: okf/0.1
---

# Abr Marquis/garrigue

## Definition (verbatim, FAO LCLR)

The land is covered by relatively dense shrubs, ocassionally interspersed with sparse trees and herbaceous vegetation.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 16E | 16F Mandatory | `LC_Shrub` | Mandatory | 20.0–100.0 | height 0.3–5.0 | LC_VegetationArtificialityCharacteristic |
| 16E | 1F5 Optional | `LC_Tree` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 16E | 1F8 Optional | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `16B`.
