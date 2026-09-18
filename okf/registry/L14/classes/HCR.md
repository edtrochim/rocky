---
id: registry:L14:HCR
kind: class
title: HCR Herbaceous crop rainfed
system: registry:L14
code: HCR
name: Herbaceous crop rainfed
status: registered
decomposed: true
file_class_id: 10F
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L14
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L14/L14.lccs
schema: okf/0.1
---

# HCR Herbaceous crop rainfed

## Definition (verbatim, FAO LCLR)

Rainfed cultivation of herbaceous crops

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 110 | 111 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed) |

Full rows: `../elements.csv`, class_id `10F`.
