---
id: registry:L49:Ca
kind: class
title: Ca Permanent crops
system: registry:L49
code: Ca
name: Permanent crops
status: registered
decomposed: true
file_class_id: '5'
n_rows: 116
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L49
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L49/L49.LChS
schema: okf/0.1
---

# Ca Permanent crops

## Definition (verbatim, FAO LCLR)

This land cover class is characterized by polygons with regular boundaries similar to crop land but usually have very tall tree crops. Permanent crops are plants that are sown or planted once and remain productive for several years, not needing to be replanted after each harvest. The permanent crop species include cocoa, rubber, cashew, palm plantations and others, mostly found in the southern and middle belt regions. Although these crops generally rely on seasonal rains, it is common practice to supply supplemental irrigation during their early establishment, usually for the first few months, to help seedlings survive dry-season stress before transitioning fully to rainfed conditions (FAO, 2016). It is composed of three stratum that defines the overall structure of the class, characterized as: •Element of trees. •Element of shrubs. •Element of herbaceous growth forms. •Vegetation artificiality in this case is defined as cultivated and managed vegetation.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 5 | 6 Fixed | `LC_Tree` | Fixed | 0–100 | height 0–200; depth -100–0; density 0–999; lengthOfTemporalRelationship 1–100 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Cultivated & Managed) |
| 5 | 19 Fixed | `LC_Shrub` | Fixed | 0–100 | height 0–200; depth -100–0; density 0–999; lengthOfTemporalRelationship 1–100 |  |
| 5 | 22 Fixed | `LC_HerbaceousGrowthForm` | Fixed | 0–100 | heightCM 0–999; density 0–999; lengthOfTemporalRelationship 1–100 |  |

Full rows: `../elements.csv`, class_id `5`.
