---
id: registry:L31:Orc
kind: class
title: Orc Orchard
system: registry:L31
code: Orc
name: Orchard
status: registered
decomposed: true
file_class_id: '18'
n_rows: 21
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L31
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L31/L31.lccs
schema: okf/0.1
---

# Orc Orchard

## Definition (verbatim, FAO LCLR)

Areas with fruit trees, mainly mango, avocado, citrus and other native species.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 19 | 1A Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed) |

Full rows: `../elements.csv`, class_id `18`.
