---
id: registry:L7:Hn
kind: class
title: Hn Aquatic Herbs Dominated
system: registry:L7
code: Hn
name: Aquatic Herbs Dominated
status: registered
decomposed: true
file_class_id: 4D
n_rows: 26
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L7
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L7/L7.lccs
schema: okf/0.1
---

# Hn Aquatic Herbs Dominated

## Definition (verbatim, FAO LCLR)

Herbaceous or aquatic vegetation in permanent or semi-permanent wetlands and swamps. Water salinity is brackish.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4E | 52 Mandatory | `LC_WaterBody` | Mandatory |  |  |  |
| 4E | 4F Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 20.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `4D`.
