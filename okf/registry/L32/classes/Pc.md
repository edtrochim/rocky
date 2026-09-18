---
id: registry:L32:Pc
kind: class
title: Pc Perennial crops
system: registry:L32
code: Pc
name: Perennial crops
status: registered
decomposed: true
file_class_id: '25'
n_rows: 17
rows_in: ../elements.csv
element_refs:
- LC_Shrub
links:
- rel: in_system
  id: registry:L32
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L32/L32.lccs
schema: okf/0.1
---

# Pc Perennial crops

## Definition (verbatim, FAO LCLR)

The class is composed of a main layer of cultivated shrubs plants. Perennial crops on agricultural land (fruit tree, coffee, tea, etc.)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 26 | 27 Mandatory | `LC_Shrub` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `25`.
