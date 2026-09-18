---
id: registry:L7:Ihc
kind: class
title: Ihc Herbaceous Crops Irrigated
system: registry:L7
code: Ihc
name: Herbaceous Crops Irrigated
status: registered
decomposed: true
file_class_id: '76'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L7
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L7/L7.lccs
schema: okf/0.1
---

# Ihc Herbaceous Crops Irrigated

## Definition (verbatim, FAO LCLR)

Cultivated agriculture with irrigated area where the growth form herb is dominant.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 77 | 78 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation) |

Full rows: `../elements.csv`, class_id `76`.
