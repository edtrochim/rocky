---
id: registry:L51:Ic
kind: class
title: Ic Irrigated croplands​
system: registry:L51
code: Ic
name: Irrigated croplands​
status: registered
decomposed: true
file_class_id: '7'
n_rows: 57
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L51
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L51/L51.LChS
schema: okf/0.1
---

# Ic Irrigated croplands​

## Definition (verbatim, FAO LCLR)

Cultivated agriculture where herbaceous crops are predominantly grown under permanent or seasonal irrigation, with water supplied (e.g. by canals, sprinklers or drip systems) to supplement or replace rainfall.​

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 7 | 12 Fixed | `LC_HerbaceousGrowthForm` | Fixed | 0–100 | heightCM 0–999; density 0–999; lengthOfTemporalRelationship 1–100 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Cultivated & Managed); LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `7`.
