---
id: registry:L12:TS
kind: class
title: TS Trees (sparse)
system: registry:L12
code: TS
name: Trees (sparse)
status: registered
decomposed: true
file_class_id: '99'
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# TS Trees (sparse)

## Definition (verbatim, FAO LCLR)

Sparse scattered trees + herbaceous natural vegetation (closed to open).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 9A | 9B Mandatory | `LC_Tree` | Mandatory | 5.0–20.0 |  | LC_VegetationArtificialityCharacteristic |
| 9A | 9E Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 50.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `99`.
