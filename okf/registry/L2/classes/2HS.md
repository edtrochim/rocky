---
id: registry:L2:2HS
kind: class
title: 2HS Sparse herbaceous
system: registry:L2
code: 2HS
name: Sparse herbaceous
status: registered
decomposed: true
file_class_id: '41'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L2
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L2/L2.lccs
schema: okf/0.1
---

# 2HS Sparse herbaceous

## Definition (verbatim, FAO LCLR)

Sparse (1-15%) short herbaceous vegetation

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 42 | 43 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 1.0–15.0 | height 3.0–30.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `41`.
