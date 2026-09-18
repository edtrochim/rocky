---
id: registry:L13:HSt
kind: class
title: HSt Herbaceous Sparse Vegetation (terrestrial)
system: registry:L13
code: HSt
name: Herbaceous Sparse Vegetation (terrestrial)
status: registered
decomposed: true
file_class_id: '18'
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L13
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L13/L13.lccs
schema: okf/0.1
---

# HSt Herbaceous Sparse Vegetation (terrestrial)

## Definition (verbatim, FAO LCLR)

Sparse herbaceous vegetation in terrestrial environment and coverage percentage is lower than 15%

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 19 | 1A Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 1.0–15.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `18`.
