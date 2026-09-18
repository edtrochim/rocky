---
id: registry:L19:1HM
kind: class
title: 1HM Herbaceous Crop Continuous Medium Fields
system: registry:L19
code: 1HM
name: Herbaceous Crop Continuous Medium Fields
status: registered
decomposed: true
file_class_id: '29'
n_rows: 20
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

# 1HM Herbaceous Crop Continuous Medium Fields

## Definition (verbatim, FAO LCLR)

Medium Sized Field(s) Of Herbaceous Crop(s)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2A | 2B Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_FieldDistribution]/name=Field Distribution, elements/LC_Characteristic[LC_FieldDistribution]/description=Describe the field distribution, elements/LC_Characteristic[LC_FieldDistribution]/type=Continuous) |

Full rows: `../elements.csv`, class_id `29`.
