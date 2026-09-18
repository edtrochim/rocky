---
id: registry:L49:Sv
kind: class
title: Sv Savanna woodland
system: registry:L49
code: Sv
name: Savanna woodland
status: registered
decomposed: true
file_class_id: '3'
n_rows: 71
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L49
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L49/L49.LChS
schema: okf/0.1
---

# Sv Savanna woodland

## Definition (verbatim, FAO LCLR)

This land cover class is characterized by the presence of two strata, which include grasslands with scattered trees. The tree density ranges between 4-10 trees per hectare (FAO, 2020). This land cover class is expressed as follows: •Coverage of herbaceous growth forms expressed in percent of plants covering the ground ranging from 40 to 100 percent. •Element of trees, with cover expressed in percent ranging from 4 to 20 percent. •Vegetation artificiality in this case is defined as natural.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3 | 3 Fixed | `LC_HerbaceousGrowthForm` | Fixed | 40–100 | heightCM 0–999; density 0–999; lengthOfTemporalRelationship 1–100 |  |
| 3 | 13 Fixed | `LC_Tree` | Fixed | 4–20 | height 0–200; depth -100–0; density 4–10; uOMArea=Hectare; lengthOfTemporalRelationship 1–100 |  |

Full rows: `../elements.csv`, class_id `3`.
