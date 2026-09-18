---
id: registry:L37:Savarbo
kind: class
title: Savarbo Tree savannah
system: registry:L37
code: Savarbo
name: Tree savannah
status: registered
decomposed: true
file_class_id: '33'
n_rows: 27
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

# Savarbo Tree savannah

## Definition (verbatim, FAO LCLR)

This formation is present in the Sudanian phytogeographic domain. It is a grouping of trees mixed with a grassy layer and shrubs. The tree coverage rate is greater than 10% but less than 50%. The tree layer has a height that varies between 10 and 20 m, with well-individualized trees scattered within the shrub layer.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 34 | 35 Mandatory | `LC_Tree` | Mandatory | 10–50 | height 10–20 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural or Seminatural) |
| 34 | 38 Mandatory | `LC_Shrub` | Mandatory | 40–100 | height 5–7 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural or Seminatural) |

Full rows: `../elements.csv`, class_id `33`.
