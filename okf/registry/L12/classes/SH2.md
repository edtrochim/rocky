---
id: registry:L12:SH2
kind: class
title: SH2 Shrubland (open)
system: registry:L12
code: SH2
name: Shrubland (open)
status: registered
decomposed: true
file_class_id: D7
n_rows: 31
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# SH2 Shrubland (open)

## Definition (verbatim, FAO LCLR)

Closed natural shrubs (H=0.5 to 1.5m), commonly observed on river valley slopes, ocassionally with scattered rocks and boulders.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| D8 | D9 Mandatory | `LC_Shrub` | Mandatory | 20.0–60.0 | height 0.5–1.5 | LC_VegetationArtificialityCharacteristic |
| D8 | DC Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 20.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `D7`.
