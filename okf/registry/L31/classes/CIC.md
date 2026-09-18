---
id: registry:L31:CIC
kind: class
title: CIC Commercial irrigated cropland
system: registry:L31
code: CIC
name: Commercial irrigated cropland
status: registered
decomposed: true
file_class_id: '9'
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L31
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L31/L31.lccs
schema: okf/0.1
---

# CIC Commercial irrigated cropland

## Definition (verbatim, FAO LCLR)

Areas covered with herbaceous irrigated crops, for commercial purposes, mainly banana, potato and tomato. Field size goes from 2 to 5 Ha.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| A | B Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation, elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_FieldSize]/description=Describe the field size) |

Full rows: `../elements.csv`, class_id `9`.
