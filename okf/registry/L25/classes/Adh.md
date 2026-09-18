---
id: registry:L25:Adh
kind: class
title: Adh Herbaceous dominated area
system: registry:L25
code: Adh
name: Herbaceous dominated area
status: registered
decomposed: true
file_class_id: '166'
n_rows: 26
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Adh Herbaceous dominated area

## Definition (verbatim, FAO LCLR)

This level corresponds to an area of natural vegetation with the mandatory presence of herbs and water body. Herbaceous growth covers 20% - 100% of the landscape.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 167 | 168 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 20.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 167 | 16B Mandatory | `LC_WaterBody` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `166`.
