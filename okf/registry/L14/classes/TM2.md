---
id: registry:L14:TM2
kind: class
title: TM2 Open trees (mixed leaf type)
system: registry:L14
code: TM2
name: Open trees (mixed leaf type)
status: registered
decomposed: true
file_class_id: FF
n_rows: 29
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L14
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L14/L14.lccs
schema: okf/0.1
---

# TM2 Open trees (mixed leaf type)

## Definition (verbatim, FAO LCLR)

Open Trees Undifferentiated (10%-40%)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 100 | 101 Mandatory | `LC_Tree` | Mandatory | 5.0–40.0 |  | LC_VegetationArtificialityCharacteristic |
| 100 | 104 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `FF`.
