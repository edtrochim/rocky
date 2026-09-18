---
id: registry:L26:SGS
kind: class
title: SGS Shrubs and grasses sparse
system: registry:L26
code: SGS
name: Shrubs and grasses sparse
status: registered
decomposed: true
file_class_id: B8
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
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
sources:
- okf/registry/_raw/L26/L26.lccs
schema: okf/0.1
---

# SGS Shrubs and grasses sparse

## Definition (verbatim, FAO LCLR)

Natural herbs with cover (0-20%) with a layer of shrubs (0-15%).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| B9 | BA Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 0.0–20.0 |  | LC_VegetationArtificialityCharacteristic |
| B9 | BD Mandatory | `LC_Shrub` | Mandatory | 0.0–15.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `B8`.
