---
id: registry:L38:CUsh
kind: class
title: CUsh Mixed unit (herbaceous crop rainfed - natural vegetation)
system: registry:L38
code: CUsh
name: Mixed unit (herbaceous crop rainfed - natural vegetation)
status: registered
decomposed: true
file_class_id: '260'
n_rows: 52
rows_in: ../elements.csv
element_refs:
- LC_GrowthForm
- LC_HerbaceousGrowthForm
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L38
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_GrowthForm
  path: ../../../vocab/elements/LC_GrowthForm.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L38/L38.lccs
schema: okf/0.1
---

# CUsh Mixed unit (herbaceous crop rainfed - natural vegetation)

## Definition (verbatim, FAO LCLR)

Areas principally occupied by agriculture interspersed in a significant fraction of natural vegetation

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 261 | 284 Mandatory | `LC_HerbaceousGrowthForm` | Temporal Sequence Depending |  | sequential_temporal_relationship/type=Sequential Other Year; sequential_temporal_relationship/length 4.0–6.0 | LC_CultivatedAndManagedVegetationCharacteristics |
| 261 | 284 Mandatory | `LC_HerbaceousGrowthForm` | Temporal Sequence Depending |  | sequential_temporal_relationship/type=Sequential Other Year; sequential_temporal_relationship/length 4.0–6.0 | LC_VegetationArtificialityCharacteristic |
| 261 | 284 Mandatory | `LC_WoodyGrowthForm` | Temporal Sequence Depending |  | sequential_temporal_relationship/type=Sequential Other Year; sequential_temporal_relationship/length 4.0–6.0 | LC_VegetationArtificialityCharacteristic |
| 264 | 265 Mandatory | `LC_GrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `260`.
