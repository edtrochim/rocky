---
id: registry:L49:Ab
kind: class
title: Ab Shrubland
system: registry:L49
code: Ab
name: Shrubland
status: registered
decomposed: true
file_class_id: '2'
n_rows: 47
rows_in: ../elements.csv
element_refs:
- LC_Shrub
links:
- rel: in_system
  id: registry:L49
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L49/L49.LChS
schema: okf/0.1
---

# Ab Shrubland

## Definition (verbatim, FAO LCLR)

This land cover class is characterized by the presence of one mandatory stratum of shrubs. The species are including but not limited to: Uvaria chamae, Picralima  nitida, Rauwolfia vomitoria, Newbouldia  laevis, Dichapetalum barteri,Rothmannia whitfieldii, Cola hispida, Glyphae brevis (Chisom et al., 2024). It is expressed as follows: •Coverage of shrubs expressed in percent of plants covering the ground ranging from 20 to 100 percent. •Vegetation artificiality in this case is defined as natural or seminatural.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2 | 2 Fixed | `LC_Shrub` | Fixed | 20–100 | height 0–200; depth -100–0; density 0–999; lengthOfTemporalRelationship 1–100 |  |

Full rows: `../elements.csv`, class_id `2`.
