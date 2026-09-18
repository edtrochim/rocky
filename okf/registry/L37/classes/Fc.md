---
id: registry:L37:Fc
kind: class
title: Fc Open forest
system: registry:L37
code: Fc
name: Open forest
status: registered
decomposed: true
file_class_id: '2'
n_rows: 26
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L37
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L37/L37.LChS
schema: okf/0.1
---

# Fc Open forest

## Definition (verbatim, FAO LCLR)

Tree formation characterized by large trees (15 to 20m high), with more or less contiguous crowns with a shrub layer which constitutes a light undergrowth. The recovery rate is between 50 and 70% with a sparse distribution. It is marked by the presence of grasses and a grassy layer.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3 | 4 Mandatory | `LC_Tree` | Mandatory | 50–70 | height 15–20 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural or Seminatural) |
| 3 | 8 Mandatory | `LC_Shrub` | Mandatory | 50–70 |  | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural or Seminatural) |

Full rows: `../elements.csv`, class_id `2`.
