---
id: registry:L19:1Torc
kind: class
title: 1Torc Irrigated Orchard
system: registry:L19
code: 1Torc
name: Irrigated Orchard
status: registered
decomposed: true
file_class_id: '12'
n_rows: 21
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

# 1Torc Irrigated Orchard

## Definition (verbatim, FAO LCLR)

Small Sized Field(s) Of Irrigated Tree Crop(s)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 13 | 14 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation, elements/LC_Characteristic[LC_Irrigation]/name=Irrigation) |

Full rows: `../elements.csv`, class_id `12`.
