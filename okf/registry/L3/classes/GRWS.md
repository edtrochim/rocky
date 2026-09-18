---
id: registry:L3:GRWS
kind: class
title: GRWS Grassland
system: registry:L3
code: GRWS
name: Grassland
status: registered
decomposed: true
file_class_id: D2
n_rows: 30
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

# GRWS Grassland

## Definition (verbatim, FAO LCLR)

Relatively dense grassland natural vegetation, with very sparse shrubs and/or trees (0-15%)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| D3 | 152 Mandatory | `LC_WoodyGrowthForm` | Mandatory | 0.1–15.0 |  | LC_VegetationArtificialityCharacteristic |
| D3 | D4 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 20.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `D2`.
