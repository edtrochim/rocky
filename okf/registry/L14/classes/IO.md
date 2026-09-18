---
id: registry:L14:IO
kind: class
title: IO Fruit tree orchards* including vineyards
system: registry:L14
code: IO
name: Fruit tree orchards* including vineyards
status: registered
decomposed: true
file_class_id: 1E
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L14
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L14/L14.lccs
schema: okf/0.1
---

# IO Fruit tree orchards* including vineyards

## Definition (verbatim, FAO LCLR)

Fruit Tree orchards mainly near water course (Jordan valley)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1F | 20 Mandatory | `LC_Tree` | Mandatory | 60.0–80.0 |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation) |

Full rows: `../elements.csv`, class_id `1E`.
