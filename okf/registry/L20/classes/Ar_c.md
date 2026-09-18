---
id: registry:L20:Ar_c
kind: class
title: Ar_c Shrubs land
system: registry:L20
code: Ar_c
name: Shrubs land
status: registered
decomposed: true
file_class_id: '49'
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

# Ar_c Shrubs land

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4A | 4B Mandatory | `LC_Shrub` | Mandatory | 65.0–100.0 | height 0.3–3.0 | LC_VegetationArtificialityCharacteristic |
| 4A | 4E Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 0.0–35.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `49`.
