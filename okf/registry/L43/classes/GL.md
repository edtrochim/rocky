---
id: registry:L43:GL
kind: class
title: GL Grassland
system: registry:L43
code: GL
name: Grassland
status: registered
decomposed: true
file_class_id: '11'
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L43
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L43/L43.lccs
schema: okf/0.1
---

# GL Grassland

## Definition (verbatim, FAO LCLR)

This level corresponds to an area of natural vegetation with the mandatory presence of herbs.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 12 | 13 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 80.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `11`.
