---
id: registry:L37:Pa
kind: class
title: Pa Agroforestry park
system: registry:L37
code: Pa
name: Agroforestry park
status: registered
decomposed: true
file_class_id: '47'
n_rows: 42
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L37
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L37/L37.LChS
schema: okf/0.1
---

# Pa Agroforestry park

## Definition (verbatim, FAO LCLR)

These are the plant formations which mainly occupy the crop fields. They result from selective deforestation when the field was opened. This plant formation can also occupy plots left fallow. Their recovery rate must be greater than 25% of the entire territory. The trees must be composed mainly of forest species. Their identification on the image essentially takes into account the agricultural territories, in particular the particular characteristics of the tree layer found there. This formation has a variable appearance depending on the rate of coverage, the nature of the species on which the shape of the crowns, the foliage and the vegetative cycle depend.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 48 | 34 Fixed | `` | Conditional Temporal | 0–100 | density 0–100000; lengthOfTemporalRelationship 1–100 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural or Seminatural) |
| 48 | 49 Mandatory | `LC_Tree` | Mandatory | 0–60 | height 2–25 |  (treePlantation=Forest Plantation); LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `47`.
