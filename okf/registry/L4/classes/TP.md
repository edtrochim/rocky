---
id: registry:L4:TP
kind: class
title: TP Tree crop plantation
system: registry:L4
code: TP
name: Tree crop plantation
status: registered
decomposed: true
file_class_id: 3E
n_rows: 27
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L4
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L4/L4.lccs
schema: okf/0.1
---

# TP Tree crop plantation

## Definition (verbatim, FAO LCLR)

Cultivated and managed cocoa and palm plantations.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3F | 40 Mandatory | `LC_Tree` | Mandatory | 0.1–70.0 |  | LC_CultivatedAndManagedVegetationCharacteristics; LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Cocoa) |

Full rows: `../elements.csv`, class_id `3E`.
