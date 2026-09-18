---
id: registry:L20:He_ar
kind: class
title: He_ar Grassland with scattered bushes
system: registry:L20
code: He_ar
name: Grassland with scattered bushes
status: registered
decomposed: true
file_class_id: '59'
n_rows: 31
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L20
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L20/L20.lccs
schema: okf/0.1
---

# He_ar Grassland with scattered bushes

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 5A | 5B Mandatory | `LC_Shrub` | Mandatory | 0.0–15.0 | height 0.3–5.0 | LC_VegetationArtificialityCharacteristic |
| 5A | 5E Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 15.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `59`.
