---
id: registry:L3:FS
kind: class
title: FS Forest Sparse
system: registry:L3
code: FS
name: Forest Sparse
status: registered
decomposed: true
file_class_id: '99'
n_rows: 29
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L3
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L3/L3.lccs
schema: okf/0.1
---

# FS Forest Sparse

## Definition (verbatim, FAO LCLR)

Woodland with sparse (<20%) trees and/or shrubs and herbaceous natural vegetation

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 9A | 14F Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 9A | 9B Mandatory | `LC_WoodyGrowthForm` | Mandatory | 5.0–20.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `99`.
