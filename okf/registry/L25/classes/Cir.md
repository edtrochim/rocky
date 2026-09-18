---
id: registry:L25:Cir
kind: class
title: Cir Regrowth shifting cultivation
system: registry:L25
code: Cir
name: Regrowth shifting cultivation
status: registered
decomposed: true
file_class_id: '203'
n_rows: 29
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Cir Regrowth shifting cultivation

## Definition (verbatim, FAO LCLR)

This class includes lands where herbaceous and/or shrub crops are cultivated temporarily, then abandoned and allowed to return to their natural vegetation while the farmer moves on to another area. It is composed of a single mandatory stratum that defines the overall structure of the class with the sequential temporal length is 2-6 years.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 204 | 205 Mandatory | `LC_Shrub` | Temporal Sequence Depending |  | sequential_temporal_relationship/type=Sequential Other Year; sequential_temporal_relationship/length 2.0–6.0; height 0.5–5.0 | LC_VegetationArtificialityCharacteristic |
| 204 | 205 Mandatory | `LC_HerbaceousGrowthForm` | Temporal Sequence Depending |  | sequential_temporal_relationship/type=Sequential Other Year; sequential_temporal_relationship/length 1.0–2.0 | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `203`.
