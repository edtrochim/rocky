---
id: registry:L25:Muhi
kind: class
title: Muhi Multiple crop - herbaceous irrigated
system: registry:L25
code: Muhi
name: Multiple crop - herbaceous irrigated
status: registered
decomposed: true
file_class_id: '262'
n_rows: 32
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Muhi Multiple crop - herbaceous irrigated

## Definition (verbatim, FAO LCLR)

This class is very basic, and generic being constituted by one mandatory stratum that defines the overall class structure. It is irrigated plantation area with multiple herbaceous crop.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 263 | 264 Mandatory | `LC_HerbaceousGrowthForm` | Temporal Sequence Depending |  | sequential_temporal_relationship/type=Sequential Same Year; sequential_temporal_relationship/length 3.0–6.0 | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation) |
| 263 | 264 Mandatory | `LC_HerbaceousGrowthForm` | Temporal Sequence Depending |  | sequential_temporal_relationship/type=Sequential Same Year; sequential_temporal_relationship/length 3.0–6.0 | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation) |

Full rows: `../elements.csv`, class_id `262`.
