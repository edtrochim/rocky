---
id: registry:L34:Ma
kind: class
title: Ma Mangrove
system: registry:L34
code: Ma
name: Mangrove
status: registered
decomposed: true
file_class_id: 2D
n_rows: 33
rows_in: ../elements.csv
element_refs:
- LC_Tree
- LC_WaterBody
links:
- rel: in_system
  id: registry:L34
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L34/L34.lccs
schema: okf/0.1
---

# Ma Mangrove

## Definition (verbatim, FAO LCLR)

This class consists of intertidal forest land. It is characterized by the presence of trees and water bodies.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2E | 33 Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Brackish) |
| 2E | 2F Mandatory | `LC_Tree` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `2D`.
