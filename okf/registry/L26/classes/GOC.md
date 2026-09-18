---
id: registry:L26:GOC
kind: class
title: GOC Grassland open to close
system: registry:L26
code: GOC
name: Grassland open to close
status: registered
decomposed: true
file_class_id: '68'
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L26
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L26/L26.lccs
schema: okf/0.1
---

# GOC Grassland open to close

## Definition (verbatim, FAO LCLR)

Natural Herbs with cover 21-80%. Optional Shrubs (0-15%).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 69 | 6A Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 21.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 69 | 6D Optional | `LC_Shrub` | Mandatory | 0.0–15.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `68`.
