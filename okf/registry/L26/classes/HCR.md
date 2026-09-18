---
id: registry:L26:HCR
kind: class
title: HCR Herbaceous crop rainfed
system: registry:L26
code: HCR
name: Herbaceous crop rainfed
status: registered
decomposed: true
file_class_id: '13'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L26
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L26/L26.lccs
schema: okf/0.1
---

# HCR Herbaceous crop rainfed

## Definition (verbatim, FAO LCLR)

Herbaceous crop rainfed

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 14 | 15 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed) |

Full rows: `../elements.csv`, class_id `13`.
