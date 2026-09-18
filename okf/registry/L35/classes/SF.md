---
id: registry:L35:SF
kind: class
title: SF Small post flooding herbaceous crops
system: registry:L35
code: SF
name: Small post flooding herbaceous crops
status: registered
decomposed: true
file_class_id: 5A
n_rows: 22
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

# SF Small post flooding herbaceous crops

## Definition (verbatim, FAO LCLR)

NA

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 5B | 5C Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_FieldSize]/name=Field Size, elements/LC_Characteristic[LC_FieldSize]/description=Describe the field size, elements/LC_Characteristic[LC_Postflooding]/name=Postflooding) |

Full rows: `../elements.csv`, class_id `5A`.
