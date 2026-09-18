---
id: registry:L6:HCR
kind: class
title: HCR Herbaceous crops rainfed
system: registry:L6
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
  id: registry:L6
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L6/L6.lccs
schema: okf/0.1
---

# HCR Herbaceous crops rainfed

## Definition (verbatim, FAO LCLR)

Rainfed agricul-ture relies only on rainfall for water, therefore NDVI values strictly de-pend on rainfall pattern over the year but the gen-eral aspect re-flects the two main crop sea-sons.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| A | B Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_Rainfed]/name=Rainfed) |

Full rows: `../elements.csv`, class_id `9`.
