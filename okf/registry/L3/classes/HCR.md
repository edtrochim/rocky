---
id: registry:L3:HCR
kind: class
title: HCR Rainfed Agriculture
system: registry:L3
code: HCR
name: Rainfed Agriculture
status: registered
decomposed: true
file_class_id: BB
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L3
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L3/L3.lccs
schema: okf/0.1
---

# HCR Rainfed Agriculture

## Definition (verbatim, FAO LCLR)

Rain-fed herbaceous crops

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| BC | BD Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed) |

Full rows: `../elements.csv`, class_id `BB`.
