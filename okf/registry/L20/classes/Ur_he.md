---
id: registry:L20:Ur_he
kind: class
title: Ur_he Dispersed urban
system: registry:L20
code: Ur_he
name: Dispersed urban
status: registered
decomposed: true
file_class_id: '77'
n_rows: 46
rows_in: ../elements.csv
element_refs:
- LC_Building
- LC_HerbaceousGrowthForm
- LC_LinearSurface
- LC_Tree
links:
- rel: in_system
  id: registry:L20
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_LinearSurface
  path: ../../../vocab/elements/LC_LinearSurface.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L20/L20.lccs
schema: okf/0.1
---

# Ur_he Dispersed urban

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 78 | 79 Mandatory | `LC_LinearSurface` | Mandatory | 0.0–10.0 |  |  |
| 78 | 126 Mandatory | `LC_Tree` | Mandatory | 0.0–30.0 | height 0.0–30.0 |  |
| 78 | 128 Mandatory | `LC_Building` | Mandatory | 15.0–30.0 |  |  |
| 78 | 7B Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 60.0–85.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `77`.
