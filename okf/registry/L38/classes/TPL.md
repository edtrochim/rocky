---
id: registry:L38:TPL
kind: class
title: TPL Tree crop plantation
system: registry:L38
code: TPL
name: Tree crop plantation
status: registered
decomposed: true
file_class_id: A9
n_rows: 21
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L38
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L38/L38.lccs
schema: okf/0.1
---

# TPL Tree crop plantation

## Definition (verbatim, FAO LCLR)

Tree crop (plantations and orchards)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| AA | AB Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation, elements/LC_Characteristic[LC_Rainfed]/name=Rainfed) |

Full rows: `../elements.csv`, class_id `A9`.
