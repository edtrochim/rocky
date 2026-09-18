---
id: registry:L28:Cbc
kind: class
title: Cbc Cultivated land herbaceous crops
system: registry:L28
code: Cbc
name: Cultivated land herbaceous crops
status: registered
decomposed: true
file_class_id: 7E
n_rows: 17
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L28
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L28/L28.lccs
schema: okf/0.1
---

# Cbc Cultivated land herbaceous crops

## Definition (verbatim, FAO LCLR)

Various herbaceous crops e.g. Cotton, vegetables, sisal, tobacco, flower plantations etc.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 7F | 80 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `7E`.
