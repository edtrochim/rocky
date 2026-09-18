---
id: registry:L3:TCP
kind: class
title: TCP Orchard and other Plantation
system: registry:L3
code: TCP
name: Orchard and other Plantation
status: registered
decomposed: true
file_class_id: '130'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L3
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L3/L3.lccs
schema: okf/0.1
---

# TCP Orchard and other Plantation

## Definition (verbatim, FAO LCLR)

Orchard crops or other plantation

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 131 | 132 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation) |

Full rows: `../elements.csv`, class_id `130`.
