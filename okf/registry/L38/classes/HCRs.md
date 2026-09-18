---
id: registry:L38:HCRs
kind: class
title: HCRs Herbaceous crop rainfed (small fields)
system: registry:L38
code: HCRs
name: Herbaceous crop rainfed (small fields)
status: registered
decomposed: true
file_class_id: '81'
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

# HCRs Herbaceous crop rainfed (small fields)

## Definition (verbatim, FAO LCLR)

Rainfed cultivation (mainly herbaceous crops with small field size), occasionally with scattered natural trees

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 82 | 1A2 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_FieldSize]/name=Field Size) |

Full rows: `../elements.csv`, class_id `81`.
