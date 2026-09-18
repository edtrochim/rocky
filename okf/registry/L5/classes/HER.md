---
id: registry:L5:HER
kind: class
title: HER Herbaceous natural vegetation
system: registry:L5
code: HER
name: Herbaceous natural vegetation
status: registered
decomposed: true
file_class_id: '36'
n_rows: 29
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L5
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L5/L5.lccs
schema: okf/0.1
---

# HER Herbaceous natural vegetation

## Definition (verbatim, FAO LCLR)

Relatively dense herba-ceous natural vegetation, occasionally with sparse shrubs and trees. NDVI values are very low throughout the year

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 37 | 38 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 37 | 3B Mandatory | `LC_WoodyGrowthForm` | Mandatory | 0.0–10.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `36`.
