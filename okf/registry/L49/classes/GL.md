---
id: registry:L49:GL
kind: class
title: GL Savanna grassland
system: registry:L49
code: GL
name: Savanna grassland
status: registered
decomposed: true
file_class_id: '20'
n_rows: 77
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L49
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L49/L49.LChS
schema: okf/0.1
---

# GL Savanna grassland

## Definition (verbatim, FAO LCLR)

This land cover class is characterized by the presence of herbaceous growth form and woody growth forms It is predominant in most parts of north part of Nigeria especially where overgrazing and wood harvest have degraded savanna woodland to largely grassland; and where erosion processes are further degrading them to bare land (Adedibu et al., 2022). It is constituted by two mandatory stratum that defines the overall class structure. •Element of herbaceous growth forms. •Cover of herbaceous growth forms is expressed in percent of plants covering the ground ranging from 40 to 100 percent. •Height of herbaceous growth forms is expressed from 1 to 3 meters. •Element of woody growth expressed ranges from 1 to 4 percent. •Vegetation artificiality is defined as natural and seminatural.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 23 | 31 Fixed | `LC_WoodyGrowthForm` | Fixed | 1–4 | height 0–200; depth -100–0; density 0–999; lengthOfTemporalRelationship 1–100 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural or Seminatural) |
| 23 | 32 Fixed | `LC_HerbaceousGrowthForm` | Fixed | 40–100 | density 0–999; lengthOfTemporalRelationship 1–100 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural or Seminatural) |

Full rows: `../elements.csv`, class_id `20`.
