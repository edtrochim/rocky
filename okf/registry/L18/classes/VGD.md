---
id: registry:L18:VGD
kind: class
title: VGD Dense natural vegetation
system: registry:L18
code: VGD
name: Dense natural vegetation
status: registered
decomposed: true
file_class_id: B
n_rows: 17
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L18
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L18/L18.lccs
schema: okf/0.1
---

# VGD Dense natural vegetation

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| D | E Mandatory | `LC_Tree` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `B`.
