---
id: registry:L42:S
kind: class
title: S Shrubland
system: registry:L42
code: S
name: Shrubland
status: registered
decomposed: true
file_class_id: '14'
n_rows: 41
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L42
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
- okf/registry/_raw/L42/L42.lccs
schema: okf/0.1
---

# S Shrubland

## Definition (verbatim, FAO LCLR)

Shrubland is a type of vegetation community characterized by the dominance of shrubs, which are woody plants shorter than trees with multiple stems and no significant trunk.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 15 | 16 Mandatory | `LC_Shrub` | Mandatory | 4.0–100.0 | height 2.0–5.0 | LC_VegetationArtificialityCharacteristic |
| 15 | 19 Optional | `LC_Tree` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 15 | 1C Optional | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `14`.
