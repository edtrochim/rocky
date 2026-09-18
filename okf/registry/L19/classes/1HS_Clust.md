---
id: registry:L19:1HS_Clust
kind: class
title: 1HS_Clust Herbaceous crop fields -small clustered
system: registry:L19
code: 1HS_Clust
name: Herbaceous crop fields -small clustered
status: registered
decomposed: true
file_class_id: '77'
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

# 1HS_Clust Herbaceous crop fields -small clustered

## Definition (verbatim, FAO LCLR)

Herbaceous Crop Fields -Small Scattered Clustered (20-50% of area).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 78 | 79 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 10.0–50.0 |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_FieldDistribution]/name=Field Distribution, elements/LC_Characteristic[LC_FieldDistribution]/description=Describe the field distribution, elements/LC_Characteristic[LC_FieldDistribution]/type=Scattered Clustered) |

Full rows: `../elements.csv`, class_id `77`.
