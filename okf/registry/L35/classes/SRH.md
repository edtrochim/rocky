---
id: registry:L35:SRH
kind: class
title: SRH Small rainfed herbaceous crops (isolated)
system: registry:L35
code: SRH
name: Small rainfed herbaceous crops (isolated)
status: registered
decomposed: true
file_class_id: 4D
n_rows: 26
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L35
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L35/L35.lccs
schema: okf/0.1
---

# SRH Small rainfed herbaceous crops (isolated)

## Definition (verbatim, FAO LCLR)

NA

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4E | 4F Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 10.0–20.0 |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_FieldSize]/name=Field Size) |

Full rows: `../elements.csv`, class_id `4D`.
