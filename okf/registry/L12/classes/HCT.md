---
id: registry:L12:HCT
kind: class
title: HCT Rainfed agriculture + rainfed orchards
system: registry:L12
code: HCT
name: Rainfed agriculture + rainfed orchards
status: registered
decomposed: true
file_class_id: AE
n_rows: 40
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# HCT Rainfed agriculture + rainfed orchards

## Definition (verbatim, FAO LCLR)

Small rainfed herbaceous crops + regular rainfed orchard plantation (usually as rows of fruit trees separating elongated fields).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| AF | B0 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_FieldSize]/name=Field Size, elements/LC_Characteristic[LC_FieldSize]/description=Describe the field size, elements/LC_Characteristic[LC_Rainfed]/name=Rainfed) |
| AF | B5 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation, elements/LC_Characteristic[LC_PlantSpreadingGeometry]/name=Plant Spreading Geometry) |

Full rows: `../elements.csv`, class_id `AE`.
