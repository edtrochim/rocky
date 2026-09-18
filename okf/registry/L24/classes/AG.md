---
id: registry:L24:AG
kind: class
title: AG Agriculture
system: registry:L24
code: AG
name: Agriculture
status: registered
decomposed: true
file_class_id: '36'
n_rows: 17
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L24
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L24/L24.lccs
schema: okf/0.1
---

# AG Agriculture

## Definition (verbatim, FAO LCLR)

Agriculture in terrestrial and aquatic/regularly flooded land.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 37 | 38 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `36`.
