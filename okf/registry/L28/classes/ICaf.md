---
id: registry:L28:ICaf
kind: class
title: ICaf Cultivated land agro-forestry system
system: registry:L28
code: ICaf
name: Cultivated land agro-forestry system
status: registered
decomposed: true
file_class_id: '72'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L28
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L28/L28.lccs
schema: okf/0.1
---

# ICaf Cultivated land agro-forestry system

## Definition (verbatim, FAO LCLR)

Home gardens with multi-storey tree covers shading other crops e.g. Banana, Coffee, beans and yams.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 73 | 74 Mandatory | `LC_WoodyGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed) |

Full rows: `../elements.csv`, class_id `72`.
