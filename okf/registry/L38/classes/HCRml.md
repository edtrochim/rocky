---
id: registry:L38:HCRml
kind: class
title: HCRml Herbaceous crop rainfed (medium/large fields)
system: registry:L38
code: HCRml
name: Herbaceous crop rainfed (medium/large fields)
status: registered
decomposed: true
file_class_id: '296'
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L38
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L38/L38.lccs
schema: okf/0.1
---

# HCRml Herbaceous crop rainfed (medium/large fields)

## Definition (verbatim, FAO LCLR)

Rainfed cultivation (mainly herbaceous crops with field size, from large to medium), occasionally with scattered natural trees

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 297 | 298 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_FieldSize]/name=Field Size) |

Full rows: `../elements.csv`, class_id `296`.
