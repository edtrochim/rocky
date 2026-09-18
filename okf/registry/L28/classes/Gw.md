---
id: registry:L28:Gw
kind: class
title: Gw Grassland wooded
system: registry:L28
code: Gw
name: Grassland wooded
status: registered
decomposed: true
file_class_id: '54'
n_rows: 29
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L28
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L28/L28.lccs
schema: okf/0.1
---

# Gw Grassland wooded

## Definition (verbatim, FAO LCLR)

Natural herbaceous cover area with some tree cover of less than 30 %.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 55 | 56 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 55 | 59 Mandatory | `LC_Tree` | Mandatory | 0.0–30.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `54`.
