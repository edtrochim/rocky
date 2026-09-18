---
id: registry:L25:Vmi
kind: class
title: Vmi Orchards (single crop) - irrigated
system: registry:L25
code: Vmi
name: Orchards (single crop) - irrigated
status: registered
decomposed: true
file_class_id: '211'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Vmi Orchards (single crop) - irrigated

## Definition (verbatim, FAO LCLR)

This class is very basic, and generic being constituted by one mandatory stratum that defines the overall class structure and it is irrigated plantation area with single tree crop.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 212 | 213 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation) |

Full rows: `../elements.csv`, class_id `211`.
