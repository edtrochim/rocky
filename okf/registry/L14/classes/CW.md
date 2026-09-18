---
id: registry:L14:CW
kind: class
title: CW Open to closed woody vegetation
system: registry:L14
code: CW
name: Open to closed woody vegetation
status: registered
decomposed: true
file_class_id: '107'
n_rows: 29
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L14
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L14/L14.lccs
schema: okf/0.1
---

# CW Open to closed woody vegetation

## Definition (verbatim, FAO LCLR)

Closed woody vegetation (40-100 %)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 108 | 109 Mandatory | `LC_WoodyGrowthForm` | Mandatory | 40.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 108 | 10C Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `107`.
