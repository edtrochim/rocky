---
id: registry:L4:FSW
kind: class
title: FSW Freshwater swamp forest
system: registry:L4
code: FSW
name: Freshwater swamp forest
status: registered
decomposed: true
file_class_id: 1D
n_rows: 34
rows_in: ../elements.csv
element_refs:
- LC_Tree
- LC_WaterBody
links:
- rel: in_system
  id: registry:L4
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L4/L4.lccs
schema: okf/0.1
---

# FSW Freshwater swamp forest

## Definition (verbatim, FAO LCLR)

Freshwater swamp land dominated by trees.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1E | 50 Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Fresh) |
| 1E | 1F Mandatory | `LC_Tree` | Mandatory | 60.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `1D`.
