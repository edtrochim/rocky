---
id: registry:L30:Abg
kind: class
title: Abg Non tree shrubland
system: registry:L30
code: Abg
name: Non tree shrubland
status: registered
decomposed: true
file_class_id: '58'
n_rows: 36
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L30
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L30/L30.lccs
schema: okf/0.1
---

# Abg Non tree shrubland

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 59 | 5A Mandatory | `LC_Shrub` | Mandatory |  | height 0.3–1.5 | LC_VegetationArtificialityCharacteristic |
| 59 | 5D Optional | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `58`.
