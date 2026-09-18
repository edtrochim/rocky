---
id: registry:L25:Cia
kind: class
title: Cia Active shifting cultivation
system: registry:L25
code: Cia
name: Active shifting cultivation
status: registered
decomposed: true
file_class_id: 1FA
n_rows: 34
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

# Cia Active shifting cultivation

## Definition (verbatim, FAO LCLR)

This class includes lands where herbaceous and/or shrub crops are cultivated temporarily. It is composed of a single mandatory stratum that defines the overall structure of the class. Rotational period is 4-6 years with sequential temporal length is 1-2 years.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1FB | 1FC Mandatory | `LC_HerbaceousGrowthForm` | Temporal Sequence Depending |  | sequential_temporal_relationship/type=Sequential Other Year; sequential_temporal_relationship/length 1.0–2.0 | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_CropRotation]/name=Crop Rotation) |
| 1FB | 1FC Mandatory | `LC_Shrub` | Temporal Sequence Depending |  | sequential_temporal_relationship/type=Sequential Other Year; sequential_temporal_relationship/length 2.0–6.0; height 0.5–5.0 | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `1FA`.
