---
id: registry:L7:H
kind: class
title: H Herbs Dominated
system: registry:L7
code: H
name: Herbs Dominated
status: registered
decomposed: true
file_class_id: 3F
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L7
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L7/L7.lccs
schema: okf/0.1
---

# H Herbs Dominated

## Definition (verbatim, FAO LCLR)

Lands with herbaceous types of cover (>20%). Tree cover < 4%. Shrub cover < 4%

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 40 | 41 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 20.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `3F`.
