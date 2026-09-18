---
id: registry:L49:Fsw
kind: class
title: Fsw Freshwater swamps
system: registry:L49
code: Fsw
name: Freshwater swamps
status: registered
decomposed: true
file_class_id: '18'
n_rows: 71
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L49
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L49/L49.LChS
schema: okf/0.1
---

# Fsw Freshwater swamps

## Definition (verbatim, FAO LCLR)

This land cover class is characterized by all vegetation along freshwater, riverbanks and marshy areas. The canopy closure ranges between 60 to 100 percent. It is composed of two stratum that defines the overall structure of the class, characterized as: •Element of woody growth forms. •Vegetation artificiality in this case defined as natural. •Artificiality of water body is natural. •Water salinity is fresh.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 20 | 28 Fixed | `LC_WaterBody` | Fixed | 0–100 | depth -100–0; persistencePeriod 0–365; density 0–999; lengthOfTemporalRelationship 1–100 | LC_WaterSalinityCharacteristic (waterSalinity=Fresh); LC_ArtificialityCharacteristic (artificiality=Natural) |
| 20 | 29 Fixed | `LC_HerbaceousGrowthForm` | Fixed | 60–100 | heightCM 0–999; density 0–999; lengthOfTemporalRelationship 1–100 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural or Seminatural) |

Full rows: `../elements.csv`, class_id `18`.
