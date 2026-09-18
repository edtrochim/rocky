---
id: registry:L5:HCR
kind: class
title: HCR Herbaceous crops rainfed
system: registry:L5
code: HCR
name: Herbaceous crops rainfed
status: registered
decomposed: true
file_class_id: '9'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L5
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L5/L5.lccs
schema: okf/0.1
---

# HCR Herbaceous crops rainfed

## Definition (verbatim, FAO LCLR)

Rainfed agricul-ture relies only on rainfall for wa-ter, therefore NDVI values strictly depend on rainfall pat-tern over the year but the gen-eral aspect re-flects the two main crop sea-sons.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| A | B Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed) |

Full rows: `../elements.csv`, class_id `9`.
