---
id: registry:L23:CRP
kind: class
title: CRP Cropland
system: registry:L23
code: CRP
name: Cropland
status: registered
decomposed: true
file_class_id: F
n_rows: 21
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L23
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L23/L23.lccs
schema: okf/0.1
---

# CRP Cropland

## Definition (verbatim, FAO LCLR)

Annual herbaceous crop - irrigated/rainfed.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 10 | 11 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_Irrigation]/name=Irrigation) |

Full rows: `../elements.csv`, class_id `F`.
