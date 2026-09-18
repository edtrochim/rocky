---
id: registry:L12:HCER
kind: class
title: HCER Rainfed agriculture, sheet erosion
system: registry:L12
code: HCER
name: Rainfed agriculture, sheet erosion
status: registered
decomposed: true
file_class_id: DF
n_rows: 25
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

# HCER Rainfed agriculture, sheet erosion

## Definition (verbatim, FAO LCLR)

Rainfed herbaceous crops with visible water sheet erosion, commonly with associated gully erosion.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| E1 | E2 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_FieldSize]/name=Field Size) |

Full rows: `../elements.csv`, class_id `DF`.
