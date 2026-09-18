---
id: registry:L38:HCS
kind: class
title: HCS Grassland
system: registry:L38
code: HCS
name: Grassland
status: registered
decomposed: true
file_class_id: 1E7
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L38
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L38/L38.lccs
schema: okf/0.1
---

# HCS Grassland

## Definition (verbatim, FAO LCLR)

Herbaceous natural vegetation with coverage from dense to sparse

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1E8 | 1E9 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 1.0–99.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `1E7`.
