---
id: registry:L12:HCSM
kind: class
title: HCSM Rainfed agriculture, sloping & mountaineous regions
system: registry:L12
code: HCSM
name: Rainfed agriculture, sloping & mountaineous regions
status: registered
decomposed: true
file_class_id: C2
n_rows: 25
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# HCSM Rainfed agriculture, sloping & mountaineous regions

## Definition (verbatim, FAO LCLR)

Rainfed herbaceous crops in sloping land and mountains (slope greater than 10 degrees) with terracing and/or contour ploughing, small and medium sized fields, sometimes with lines of shrubs demarcating fields.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| C3 | C4 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_FieldSize]/name=Field Size) |

Full rows: `../elements.csv`, class_id `C2`.
