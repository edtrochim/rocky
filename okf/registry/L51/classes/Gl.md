---
id: registry:L51:Gl
kind: class
title: Gl Grasslands​
system: registry:L51
code: Gl
name: Grasslands​
status: registered
decomposed: true
file_class_id: '4'
n_rows: 115
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L51
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
- okf/registry/_raw/L51/L51.LChS
schema: okf/0.1
---

# Gl Grasslands​

## Definition (verbatim, FAO LCLR)

Land area with herbaceous types of cover (>10%). Tree cover < 10%. Shrub cover < 10%​

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4 | 6 Fixed | `LC_HerbaceousGrowthForm` | Fixed | 10–100 | heightCM 0–999; density 0–999; lengthOfTemporalRelationship 1–100 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural) |
| 4 | 7 Optional | `LC_Tree` | Fixed | 0–10 | height 0–200; depth -100–0; density 0–999; lengthOfTemporalRelationship 1–100 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural) |
| 4 | 8 Optional | `LC_Shrub` | Fixed | 0–10 | height 0–200; depth -100–0; density 0–999; lengthOfTemporalRelationship 1–100 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural) |

Full rows: `../elements.csv`, class_id `4`.
