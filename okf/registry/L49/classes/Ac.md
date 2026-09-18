---
id: registry:L49:Ac
kind: class
title: Ac Open forest
system: registry:L49
code: Ac
name: Open forest
status: registered
decomposed: true
file_class_id: '19'
n_rows: 49
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L49
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L49/L49.LChS
schema: okf/0.1
---

# Ac Open forest

## Definition (verbatim, FAO LCLR)

This land cover class is characterized by the presence of one mandatory tree stratum that defines the overall class structure.  The canopy can be two or three layers but usually the topmost layer comprises of scattered trees, and the canopy closure. This is usually referred to as secondary vegetation (FAO, 2020). It is expressed as follows: •Coverage of trees between 15 to 70 percent. •Vegetation artificiality is natural to semi-natural vegetation.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 21 | 30 Fixed | `LC_Tree` | Fixed | 15–70 | height 0–200; depth -100–0; density 0–999; lengthOfTemporalRelationship 1–100 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural or Seminatural) |

Full rows: `../elements.csv`, class_id `19`.
