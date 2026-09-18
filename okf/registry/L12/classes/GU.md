---
id: registry:L12:GU
kind: class
title: GU Gullies
system: registry:L12
code: GU
name: Gullies
status: registered
decomposed: true
file_class_id: 4B
n_rows: 24
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_Tree
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# GU Gullies

## Definition (verbatim, FAO LCLR)

Gully erosion, commonly associated with river beds, occasionally with trees and/or tall shrubs.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4D | 4E Mandatory | `LC_BareSoil` | Mandatory |  |  |  |
| 4D | 4E Mandatory | `LC_Tree` | Optional |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `4B`.
