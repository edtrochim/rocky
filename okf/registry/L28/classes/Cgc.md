---
id: registry:L28:Cgc
kind: class
title: Cgc Cultivated land grain crops
system: registry:L28
code: Cgc
name: Cultivated land grain crops
status: registered
decomposed: true
file_class_id: '83'
n_rows: 17
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L28
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L28/L28.lccs
schema: okf/0.1
---

# Cgc Cultivated land grain crops

## Definition (verbatim, FAO LCLR)

Various types of grass crops e.g., maize, wheat, millet, rice, sorghum.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 84 | 85 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `83`.
