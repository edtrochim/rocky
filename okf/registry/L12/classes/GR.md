---
id: registry:L12:GR
kind: class
title: GR Grassland
system: registry:L12
code: GR
name: Grassland
status: registered
decomposed: true
file_class_id: D2
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# GR Grassland

## Definition (verbatim, FAO LCLR)

Relatively dense natural vegetation, occasionally with sparse shrubs.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| D3 | D4 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 15.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `D2`.
