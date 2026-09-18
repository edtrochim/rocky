---
id: registry:L26:TCI
kind: class
title: TCI Tree crop irrigated
system: registry:L26
code: TCI
name: Tree crop irrigated
status: registered
decomposed: true
file_class_id: '6'
n_rows: 21
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L26
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L26/L26.lccs
schema: okf/0.1
---

# TCI Tree crop irrigated

## Definition (verbatim, FAO LCLR)

Tree crops, orchards and other tree plantation irrigated.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 7 | 8 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation) |

Full rows: `../elements.csv`, class_id `6`.
