---
id: registry:L49:Ad
kind: class
title: Ad Closed forest
system: registry:L49
code: Ad
name: Closed forest
status: registered
decomposed: true
file_class_id: '1'
n_rows: 47
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

# Ad Closed forest

## Definition (verbatim, FAO LCLR)

This land cover is characterized by the presence of evergreen plants of high species diversity; the canopy can be of three layers with the emergent layer of 24-50 meters high. The middle layer (16-40 m high) is also discontinuous but taken together with the upper layer. The lower tree layer (10-16m high) forms a continuous canopy. Below the trees are the shrubs and herbaceaou layers containing young trees and seedlings. This land cover can be found in south part of Nigeria (FAO, 2020). It is expressed as follow: •Coverage of trees between 70 to 100 percent. •Vegetation artificiality is natural to semi-natural vegetation.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1 | 1 Fixed | `LC_Tree` | Fixed | 70–100 | height 10–50; depth -100–0; woodyLeafPhenology=Evergreen; density 0–999; lengthOfTemporalRelationship 1–100 |  |

Full rows: `../elements.csv`, class_id `1`.
