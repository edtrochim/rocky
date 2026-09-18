---
id: registry:L51:Cf
kind: class
title: Cf Closed forest​
system: registry:L51
code: Cf
name: Closed forest​
status: registered
decomposed: true
file_class_id: '1'
n_rows: 87
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L51
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L51/L51.LChS
schema: okf/0.1
---

# Cf Closed forest​

## Definition (verbatim, FAO LCLR)

Land area with tree cover from 70 to 100 %. Undifferentiated trees, sometimes mixed broadleaved and needle-leaved; occasionally with shrubs.​

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1 | 1 Fixed | `LC_Tree` | Fixed | 70–100 | height 0–200; depth -100–0; density 0–999; lengthOfTemporalRelationship 1–100 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural) |
| 1 | 2 Optional | `LC_Shrub` | Fixed | 0–100 | height 0–200; depth -100–0; density 0–999; lengthOfTemporalRelationship 1–100 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural) |

Full rows: `../elements.csv`, class_id `1`.
