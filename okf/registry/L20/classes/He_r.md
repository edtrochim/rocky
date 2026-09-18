---
id: registry:L20:He_r
kind: class
title: He_r Grassland with rock outcrop
system: registry:L20
code: He_r
name: Grassland with rock outcrop
status: registered
decomposed: true
file_class_id: '70'
n_rows: 27
rows_in: ../elements.csv
element_refs:
- LC_BareRock
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L20
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareRock
  path: ../../../vocab/elements/LC_BareRock.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L20/L20.lccs
schema: okf/0.1
---

# He_r Grassland with rock outcrop

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 71 | 72 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 60.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 71 | 75 Mandatory | `LC_BareRock` | Mandatory | 0.0–10.0 |  |  |

Full rows: `../elements.csv`, class_id `70`.
