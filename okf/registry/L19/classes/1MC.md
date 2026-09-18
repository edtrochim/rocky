---
id: registry:L19:1MC
kind: class
title: 1MC Multiple Crop - Agroforest
system: registry:L19
code: 1MC
name: Multiple Crop - Agroforest
status: registered
decomposed: true
file_class_id: 4F
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L19
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L19/L19.lccs
schema: okf/0.1
---

# 1MC Multiple Crop - Agroforest

## Definition (verbatim, FAO LCLR)

Field(s) Of Tree Crop(s) .

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 50 | 51 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation) |

Full rows: `../elements.csv`, class_id `4F`.
