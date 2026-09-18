---
id: registry:L11:Vi
kind: class
title: Vi Villages
system: registry:L11
code: Vi
name: Villages
status: registered
decomposed: true
file_class_id: 5E
n_rows: 34
rows_in: ../elements.csv
element_refs:
- LC_Building
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L11
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L11/L11.lccs
schema: okf/0.1
---

# Vi Villages

## Definition (verbatim, FAO LCLR)

Low-density urban built-up areas + small cultivated herbaceous crops and/or orchards and other plantation.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 5F | 60 Mandatory | `LC_Building` | Mandatory |  | portioning 30.0–50.0 |  |
| 5F | 60 Mandatory | `LC_Tree` | Optional |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation) |
| 5F | 60 Mandatory | `LC_HerbaceousGrowthForm` | Optional |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_FieldSize]/name=Field Size, elements/LC_Characteristic[LC_FieldSize]/description=Describe the field size) |

Full rows: `../elements.csv`, class_id `5E`.
