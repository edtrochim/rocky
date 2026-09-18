---
id: registry:L19:1MixU
kind: class
title: 1MixU Complex Units
system: registry:L19
code: 1MixU
name: Complex Units
status: registered
decomposed: true
file_class_id: '55'
n_rows: 53
rows_in: ../elements.csv
element_refs:
- LC_BuiltUpSurface
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L19
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BuiltUpSurface
  path: ../../../vocab/elements/LC_BuiltUpSurface.md
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
- okf/registry/_raw/L19/L19.lccs
schema: okf/0.1
---

# 1MixU Complex Units

## Definition (verbatim, FAO LCLR)

Complex units present mainly along the canals formed by Small Sized Field(s) Of Irrigated Tree Crop(s) with Permanently Cropped Area with Small Field(s) of Shrub Crops and Rural houses.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 56 | 57 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation) |
| 56 | 61 Mandatory | `LC_BuiltUpSurface` | Mandatory |  |  | LC_ConstructionUse (type=Rural houses) |
| 56 | 5B Mandatory | `LC_Shrub` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |
| 56 | 5E Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `55`.
