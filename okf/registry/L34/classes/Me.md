---
id: registry:L34:Me
kind: class
title: Me Meadow
system: registry:L34
code: Me
name: Meadow
status: registered
decomposed: true
file_class_id: 1E
n_rows: 28
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L34
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L34/L34.lccs
schema: okf/0.1
---

# Me Meadow

## Definition (verbatim, FAO LCLR)

This land consists of relatively dense herbaceous natural vegetation, occasionally populated by sparse shrubs and trees.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1F | 20 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |
| 1F | 23 Mandatory | `LC_WoodyGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `1E`.
