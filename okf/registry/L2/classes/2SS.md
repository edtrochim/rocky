---
id: registry:L2:2SS
kind: class
title: 2SS Sparse shrubs with sparse herbaceous
system: registry:L2
code: 2SS
name: Sparse shrubs with sparse herbaceous
status: registered
decomposed: true
file_class_id: '61'
n_rows: 32
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L2
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L2/L2.lccs
schema: okf/0.1
---

# 2SS Sparse shrubs with sparse herbaceous

## Definition (verbatim, FAO LCLR)

Sparse (1-15%) shrubs with sparse (1-15%) herbaceous

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 62 | 63 Mandatory | `LC_Shrub` | Mandatory | 1.0–15.0 | height 0.03–5.0 | LC_VegetationArtificialityCharacteristic |
| 62 | 10E Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 5.0–15.0 | height 3.0–300.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `61`.
