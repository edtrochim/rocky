---
id: registry:L35:SSC
kind: class
title: SSC Scattered isolated small sized field(s) of rainfed shrub crop(s)
system: registry:L35
code: SSC
name: Scattered isolated small sized field(s) of rainfed shrub crop(s)
status: registered
decomposed: true
file_class_id: '30'
n_rows: 25
rows_in: ../elements.csv
element_refs:
- LC_Shrub
links:
- rel: in_system
  id: registry:L35
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L35/L35.lccs
schema: okf/0.1
---

# SSC Scattered isolated small sized field(s) of rainfed shrub crop(s)

## Definition (verbatim, FAO LCLR)

NA

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 31 | 32 Mandatory | `LC_Shrub` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_FieldSize]/name=Field Size) |

Full rows: `../elements.csv`, class_id `30`.
