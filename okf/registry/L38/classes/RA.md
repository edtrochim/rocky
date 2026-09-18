---
id: registry:L38:RA
kind: class
title: RA Rural settlement
system: registry:L38
code: RA
name: Rural settlement
status: registered
decomposed: true
file_class_id: 22B
n_rows: 41
rows_in: ../elements.csv
element_refs:
- LC_BuiltUpSurface
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L38
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BuiltUpSurface
  path: ../../../vocab/elements/LC_BuiltUpSurface.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L38/L38.lccs
schema: okf/0.1
---

# RA Rural settlement

## Definition (verbatim, FAO LCLR)

Low density urban built-up areas interspersed with small cultivated herbaceous crops and/or orchards

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 233 | 234 Optional | `LC_Tree` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 22C | 22D Mandatory | `LC_BuiltUpSurface` | Mandatory | 5.0–40.0 |  |  |
| 22F | 230 Optional | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `22B`.
