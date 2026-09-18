---
id: registry:L8:SC
kind: class
title: SC Shifting cultivation
system: registry:L8
code: SC
name: Shifting cultivation
status: registered
decomposed: true
file_class_id: 18D
n_rows: 37
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L8
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L8/L8.lccs
schema: okf/0.1
---

# SC Shifting cultivation

## Definition (verbatim, FAO LCLR)

This class includes lands where herbaceous crops are cultivated temporarily, then abandoned and allowed to return to their natural vegetation while the farmer moves on to another area.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 18E | 2D5 Mandatory | `LC_HerbaceousGrowthForm` | Temporal Sequence Depending |  | sequential_temporal_relationship/type=Sequential Other Year; sequential_temporal_relationship/length 1.0–2.0 | LC_CultivatedAndManagedVegetationCharacteristics |
| 18E | 2D5 Mandatory | `LC_HerbaceousGrowthForm` | Temporal Sequence Depending |  | sequential_temporal_relationship/type=Sequential Other Year; sequential_temporal_relationship/length 3.0–4.0 | LC_VegetationArtificialityCharacteristic |
| 18E | 2D5 Mandatory | `LC_Shrub` | Temporal Sequence Depending |  | sequential_temporal_relationship/type=Sequential Other Year; sequential_temporal_relationship/length 4.0–7.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `18D`.
