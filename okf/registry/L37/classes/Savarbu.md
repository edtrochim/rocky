---
id: registry:L37:Savarbu
kind: class
title: Savarbu Shrub savannah
system: registry:L37
code: Savarbu
name: Shrub savannah
status: registered
decomposed: true
file_class_id: '53'
n_rows: 36
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L37
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
- okf/registry/_raw/L37/L37.LChS
schema: okf/0.1
---

# Savarbu Shrub savannah

## Definition (verbatim, FAO LCLR)

This type of savannah is characterized by the dominance of shrub species with a coverage of between 10 and 50%. The shrubs are between 4 and 7 m high and are overlooked by a few rare trees scattered here and there, whose coverage is less than 10%. A high herbaceous stratum (1 to 1.5 m) and a lower stratum also occupy this plant formation. Its recognition in images is not always easy because of the physiognomic variability created according to the climatic seasons and which has an effect on reflectance.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 54 | 55 Mandatory | `LC_Shrub` | Mandatory | 10–50 | height 4–7 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural or Seminatural) |
| 54 | 58 Mandatory | `LC_Tree` | Mandatory | 0–10 | height 1–10 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural or Seminatural) |
| 54 | 61 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  | height 100–150 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural or Seminatural) |

Full rows: `../elements.csv`, class_id `53`.
