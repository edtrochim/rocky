---
id: registry:L51:Rc
kind: class
title: Rc Rainfed croplands​
system: registry:L51
code: Rc
name: Rainfed croplands​
status: registered
decomposed: true
file_class_id: '6'
n_rows: 77
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L51
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L51/L51.LChS
schema: okf/0.1
---

# Rc Rainfed croplands​

## Definition (verbatim, FAO LCLR)

Land area covered with temporary rainfed herbaceous crops followed by harvest and a bare soil period.​

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 6 | 10 Fixed | `LC_HerbaceousGrowthForm` | Conditional Temporal | 0–100 | heightCM 0–999; density 0–999; lengthOfTemporalRelationship 1–100 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Cultivated & Managed); LC_CultivatedAndManagedVegetationCharacteristics (irrigationType=Surface) |
| 6 | 11 Fixed | `LC_BareSoil` | Fixed | 0–100 | height 0–200; density 0–999; lengthOfTemporalRelationship 1–100 |  |

Full rows: `../elements.csv`, class_id `6`.
