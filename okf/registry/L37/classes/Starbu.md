---
id: registry:L37:Starbu
kind: class
title: Starbu Shrub steppe
system: registry:L37
code: Starbu
name: Shrub steppe
status: registered
decomposed: true
file_class_id: '64'
n_rows: 27
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L37
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L37/L37.LChS
schema: okf/0.1
---

# Starbu Shrub steppe

## Definition (verbatim, FAO LCLR)

This unit has the same structure as the tree steppe, marked by the alternation of vegetation and bare soil. However, in the present case, the vegetation consists of the shrub layer (4 to 6 m).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 65 | 66 Mandatory | `LC_Shrub` | Mandatory | 4–10 | height 4–6 | LC_VegetationArtificialityCharacteristic |
| 65 | 69 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 20–50 | height 10–80 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `64`.
