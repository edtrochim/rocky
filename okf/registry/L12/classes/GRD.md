---
id: registry:L12:GRD
kind: class
title: GRD Grassland - degraded
system: registry:L12
code: GRD
name: Grassland - degraded
status: registered
decomposed: true
file_class_id: 10E
n_rows: 26
rows_in: ../elements.csv
element_refs:
- LC_BareRock
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareRock
  path: ../../../vocab/elements/LC_BareRock.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# GRD Grassland - degraded

## Definition (verbatim, FAO LCLR)

Degraded grassland with low vegetation cover, ocassionally bare with scattered rock outcrops; noticeably in sloping areas adjacent to main river valley.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 110 | 111 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 0.0–15.0 |  | LC_VegetationArtificialityCharacteristic |
| 110 | 111 Mandatory | `LC_BareRock` | Optional | 0.0–5.0 |  |  |

Full rows: `../elements.csv`, class_id `10E`.
