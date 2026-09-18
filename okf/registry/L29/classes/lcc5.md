---
id: registry:L29:lcc5
kind: class
title: lcc5 Other wooded land
system: registry:L29
code: lcc5
name: Other wooded land
status: registered
decomposed: true
file_class_id: '42'
n_rows: 20
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L29
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L29/L29.lccs
schema: okf/0.1
---

# lcc5 Other wooded land

## Definition (verbatim, FAO LCLR)

Land not classified as forest spanning more than 0.5 ha, having at least 20 m width and a tree canopy cover of trees between 5% and 10%. Or The canopy cover of trees less than 5% but the combined cover of shrubs, bushes and trees more than 10%; includes area of shrubs and bushes where no trees are present.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 43 | 44 Mandatory | `LC_Tree` | Mandatory | 5.0–10.0 | height 5.0–50.0 |  |
| 43 | 44 Mandatory | `LC_Shrub` | Optional |  |  |  |

Full rows: `../elements.csv`, class_id `42`.
