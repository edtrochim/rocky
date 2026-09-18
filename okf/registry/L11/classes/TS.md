---
id: registry:L11:TS
kind: class
title: TS Trees sparse
system: registry:L11
code: TS
name: Trees sparse
status: registered
decomposed: true
file_class_id: '107'
n_rows: 29
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L11
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L11/L11.lccs
schema: okf/0.1
---

# TS Trees sparse

## Definition (verbatim, FAO LCLR)

Sparse scattered trees (0%-20%) + herbaceous natural vegetation.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 108 | 10C Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 108 | 13B Mandatory | `LC_Tree` | Mandatory | 5.0–20.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `107`.
