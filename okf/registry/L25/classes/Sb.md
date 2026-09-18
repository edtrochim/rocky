---
id: registry:L25:Sb
kind: class
title: Sb Woody dominated area
system: registry:L25
code: Sb
name: Woody dominated area
status: registered
decomposed: true
file_class_id: 10B
n_rows: 26
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Sb Woody dominated area

## Definition (verbatim, FAO LCLR)

It corresponds to areas with natural semi-natural vegetation where the growth form woody is dominant. The cover % of the element woody is >20% (cover ranging from 20 to 100%). The presence of non-vegetated area i.e., water body is recognized in this area.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 10C | 110 Mandatory | `LC_WaterBody` | Mandatory |  |  |  |
| 10C | 10D Mandatory | `LC_WoodyGrowthForm` | Mandatory | 20.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `10B`.
