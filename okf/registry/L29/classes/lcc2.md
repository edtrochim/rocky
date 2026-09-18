---
id: registry:L29:lcc2
kind: class
title: lcc2 Cropland
system: registry:L29
code: lcc2
name: Cropland
status: registered
decomposed: true
file_class_id: '20'
n_rows: 53
rows_in: ../elements.csv
element_refs:
- LC_Forbs
- LC_Graminoid
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L29
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Forbs
  path: ../../../vocab/elements/LC_Forbs.md
- rel: uses_type
  id: element:LC_Graminoid
  path: ../../../vocab/elements/LC_Graminoid.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L29/L29.lccs
schema: okf/0.1
---

# lcc2 Cropland

## Definition (verbatim, FAO LCLR)

This category includes arable and tillage land, and agroforestry systems where vegetation falls below the thresholds used for the forest land category, consistent with the selection of national definitions.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 21 | 22 Mandatory | `LC_Graminoid` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |
| 21 | 22 Mandatory | `LC_Forbs` | Optional |  |  | LC_CultivatedAndManagedVegetationCharacteristics |
| 21 | 26 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation) |
| 21 | 2A Mandatory | `LC_Graminoid` | Mandatory |  |  |  |
| 21 | 2A Mandatory | `LC_Forbs` | Optional |  |  |  |
| 21 | 2A Mandatory | `LC_Shrub` | Optional |  |  |  |

Full rows: `../elements.csv`, class_id `20`.
