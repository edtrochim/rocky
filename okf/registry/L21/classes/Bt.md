---
id: registry:L21:Bt
kind: class
title: Bt Village
system: registry:L21
code: Bt
name: Village
status: registered
decomposed: true
file_class_id: B4
n_rows: 28
rows_in: ../elements.csv
element_refs:
- LC_Building
- LC_Tree
links:
- rel: in_system
  id: registry:L21
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L21/L21.lccs
schema: okf/0.1
---

# Bt Village

## Definition (verbatim, FAO LCLR)

The patch of land with houses and garden surrounding house.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| B5 | B6 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation) |
| B5 | BA Mandatory | `LC_Building` | Mandatory |  | construction_material=Hard Material |  |

Full rows: `../elements.csv`, class_id `B4`.
