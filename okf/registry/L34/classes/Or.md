---
id: registry:L34:Or
kind: class
title: Or Orchard
system: registry:L34
code: Or
name: Orchard
status: registered
decomposed: true
file_class_id: '43'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L34
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L34/L34.lccs
schema: okf/0.1
---

# Or Orchard

## Definition (verbatim, FAO LCLR)

This land consists of orchards cultivated for the production of fruits (i.e. organge, citrus, fig, apple, peach and apricot) or other types of plantations.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 44 | 45 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation) |

Full rows: `../elements.csv`, class_id `43`.
