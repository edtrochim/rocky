---
id: registry:L49:Can
kind: class
title: Can Annual crops
system: registry:L49
code: Can
name: Annual crops
status: registered
decomposed: true
file_class_id: '23'
n_rows: 106
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
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
sources:
- okf/registry/_raw/L49/L49.LChS
schema: okf/0.1
---

# Can Annual crops

## Definition (verbatim, FAO LCLR)

This land cover class is characterized by the plants that complete their life cycle from planting to harvesting within a single growing season, typically less than one year. These crops are sown and harvested in the same year and require replanting for each subsequent season. Common examples include cassava, maize, rice, millet, groundnut, cowpea and others. Some annuals are grown under irrigation using systems like sprinklers or drip to ensure consistent moisture and extend cultivation into drier periods (FAO, 2016). It is composed of two stratum that defines the overall structure of the class, characterized as: •Element of herbaceous growth forms. •Element of shrubs. •Vegetation artificiality in this case is defined as cultivated and managed vegetation.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 26 | 35 Fixed | `LC_HerbaceousGrowthForm` | Fixed | 0–100 | heightCM 0–999; density 0–999; lengthOfTemporalRelationship 1–100 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Cultivated & Managed); LC_CultivatedAndManagedVegetationCharacteristics (irrigationType=Sprinkler) |
| 26 | 35 Fixed | `LC_Shrub` | Fixed | 0–100 | height 0–200; depth -100–0; density 0–999; temporalType=Sequential Same Year; lengthOfTemporalRelationship 1–100; lengthOfTemporalRelationshipUnits=Year | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Cultivated & Managed); LC_CultivatedAndManagedVegetationCharacteristics (irrigationType=Sprinkler) |

Full rows: `../elements.csv`, class_id `23`.
