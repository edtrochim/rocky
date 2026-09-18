---
id: registry:L3:FO
kind: class
title: FO Forest Open
system: registry:L3
code: FO
name: Forest Open
status: registered
decomposed: true
file_class_id: 7A
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

# FO Forest Open

## Definition (verbatim, FAO LCLR)

Woodland with open (20-60%) trees and/or shrubs and herbaceous natural vegetation

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 7B | 14A Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 7B | 7C Mandatory | `LC_WoodyGrowthForm` | Mandatory | 20.0–60.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `7A`.
