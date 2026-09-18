---
id: registry:L19:1HS_Isol
kind: class
title: 1HS_Isol Agricultural fields Scattered Isolated
system: registry:L19
code: 1HS_Isol
name: Agricultural fields Scattered Isolated
status: registered
decomposed: true
file_class_id: '71'
n_rows: 21
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L19
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L19/L19.lccs
schema: okf/0.1
---

# 1HS_Isol Agricultural fields Scattered Isolated

## Definition (verbatim, FAO LCLR)

Scattered Isolated Field(s) Of Herbaceous Crop(s)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 72 | 73 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 10.0–20.0 |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_FieldDistribution]/name=Field Distribution, elements/LC_Characteristic[LC_FieldDistribution]/description=Describe the field distribution, elements/LC_Characteristic[LC_FieldDistribution]/type=Scattered Isolated) |

Full rows: `../elements.csv`, class_id `71`.
