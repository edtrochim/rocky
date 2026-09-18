---
id: registry:L26:WOC
kind: class
title: WOC Woodland open to close
system: registry:L26
code: WOC
name: Woodland open to close
status: registered
decomposed: true
file_class_id: C4
n_rows: 42
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L26
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
- okf/registry/_raw/L26/L26.lccs
schema: okf/0.1
---

# WOC Woodland open to close

## Definition (verbatim, FAO LCLR)

Natural shrubs with cover 40-100% with a layer of trees (15-30%) and herbs (0-50%).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| C5 | C6 Mandatory | `LC_Shrub` | Mandatory | 40.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| C5 | C9 Mandatory | `LC_Tree` | Mandatory | 15.0–30.0 |  | LC_VegetationArtificialityCharacteristic |
| C5 | CC Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 0.0–50.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `C4`.
