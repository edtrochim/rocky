---
id: registry:L25:Cih
kind: class
title: Cih Herbeceous crop dominated
system: registry:L25
code: Cih
name: Herbeceous crop dominated
status: registered
decomposed: true
file_class_id: '256'
n_rows: 19
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

# Cih Herbeceous crop dominated

## Definition (verbatim, FAO LCLR)

It corresponds to areas with cultivated irrigated agriculture where the growth form herb is dominant.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 257 | 258 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation) |

Full rows: `../elements.csv`, class_id `256`.
