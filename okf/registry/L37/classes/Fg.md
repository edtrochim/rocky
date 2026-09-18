---
id: registry:L37:Fg
kind: class
title: Fg Gallery forest
system: registry:L37
code: Fg
name: Gallery forest
status: registered
decomposed: true
file_class_id: '11'
n_rows: 37
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

# Fg Gallery forest

## Definition (verbatim, FAO LCLR)

Linear in shape, this plant formation runs along watercourses and appears as a riparian barrier and is made up of tree species or deciduous forest. It is sometimes destroyed in places for the benefit of agricultural developments. It is easily identifiable in the image by its shape and tone which generally contrasts with the immediate environment when the latter has been degraded by man.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 12 | 13 Mandatory | `LC_Tree` | Mandatory | 40–65 | height 3–30 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural or Seminatural) |
| 12 | 16 Mandatory | `LC_Shrub` | Mandatory | 15–65 | height 0–5 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural or Seminatural) |
| 12 | 19 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 15–100 | height 3–300 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural or Seminatural) |

Full rows: `../elements.csv`, class_id `11`.
