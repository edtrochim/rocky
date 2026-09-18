---
id: registry:L2:2SSd
kind: class
title: 2SSd Sparse dwarf shrubs with sparse herbaceous
system: registry:L2
code: 2SSd
name: Sparse dwarf shrubs with sparse herbaceous
status: registered
decomposed: true
file_class_id: '68'
n_rows: 28
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

# 2SSd Sparse dwarf shrubs with sparse herbaceous

## Definition (verbatim, FAO LCLR)

Sparse (1-15%) dwarf (< 0,5 m) shrubs with sparse (1-15%) herbaceous

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 69 | 6A Mandatory | `LC_Shrub` | Mandatory | 1.0–15.0 | height 0.1–0.5 | LC_VegetationArtificialityCharacteristic |
| 69 | 6A Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 5.0–15.0 | height 3.0–30.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `68`.
