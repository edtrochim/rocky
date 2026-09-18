---
id: registry:L45:Sa
kind: class
title: Sa Tree savanna
system: registry:L45
code: Sa
name: Tree savanna
status: registered
decomposed: true
file_class_id: '20'
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L45
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L45/L45.lccs
schema: okf/0.1
---

# Sa Tree savanna

## Definition (verbatim, FAO LCLR)

Lands with herbaceous types of cover. Tree cover between 4–20%.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 21 | 22 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 40.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 21 | 25 Mandatory | `LC_Tree` | Mandatory | 4.0–20.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `20`.
