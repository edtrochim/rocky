---
id: registry:L6:ORC
kind: class
title: ORC Tree orchards
system: registry:L6
code: ORC
name: Tree orchards
status: registered
decomposed: true
file_class_id: F
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L6
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L6/L6.lccs
schema: okf/0.1
---

# ORC Tree orchards

## Definition (verbatim, FAO LCLR)

Orchards are areas cultivated for the production of fruits, nuts, and other type of plan-tations. Areas cov-ered by orchards are characterized by NDVI values very similar to the one shown by tree closed land cover class.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 10 | 11 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation) |

Full rows: `../elements.csv`, class_id `F`.
