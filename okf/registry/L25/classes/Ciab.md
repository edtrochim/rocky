---
id: registry:L25:Ciab
kind: class
title: Ciab Shrub crop dominated
system: registry:L25
code: Ciab
name: Shrub crop dominated
status: registered
decomposed: true
file_class_id: '250'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_Shrub
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Ciab Shrub crop dominated

## Definition (verbatim, FAO LCLR)

It corresponds to areas with cultivated irrigated agriculture where the growth form shrub is dominant.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 251 | 252 Mandatory | `LC_Shrub` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation) |

Full rows: `../elements.csv`, class_id `250`.
