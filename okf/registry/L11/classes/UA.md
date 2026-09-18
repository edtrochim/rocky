---
id: registry:L11:UA
kind: class
title: UA Urban area
system: registry:L11
code: UA
name: Urban area
status: registered
decomposed: true
file_class_id: E
n_rows: 23
rows_in: ../elements.csv
element_refs:
- LC_Building
- LC_Tree
links:
- rel: in_system
  id: registry:L11
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L11/L11.lccs
schema: okf/0.1
---

# UA Urban area

## Definition (verbatim, FAO LCLR)

Larger high-density urban built-up area occasionally with trees/plantation.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| F | 10 Mandatory | `LC_Building` | Mandatory |  |  |  |
| F | 10 Mandatory | `LC_Tree` | Optional |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation) |

Full rows: `../elements.csv`, class_id `E`.
