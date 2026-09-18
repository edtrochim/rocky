---
id: registry:L37:Vg
kind: class
title: Vg Orchard
system: registry:L37
code: Vg
name: Orchard
status: registered
decomposed: true
file_class_id: '105'
n_rows: 17
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L37
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L37/L37.LChS
schema: okf/0.1
---

# Vg Orchard

## Definition (verbatim, FAO LCLR)

These are plots planted with fruit trees; pure crops or mixture of fruit species, fruit trees in association with areas always covered with grass. Satellite images are only suitable for recognizing orchards and fruit plantations based on their geometric shape printed by man if they are large. The use of exogenous data (aerial photographs, topographical maps) and field campaigns are essential for their recognition. Citrus fruits, mango trees, papayas, banana trees, cashews etc. are included in this class.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 106 | 107 Mandatory | `LC_Tree` | Mandatory |  |  |  (orchardAndOtherPlantation=Orchard And Other Plantation); LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `105`.
