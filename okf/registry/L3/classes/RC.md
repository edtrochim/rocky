---
id: registry:L3:RC
kind: class
title: RC Rice Crop
system: registry:L3
code: RC
name: Rice Crop
status: registered
decomposed: true
file_class_id: '136'
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

# RC Rice Crop

## Definition (verbatim, FAO LCLR)

Irrigated rice crop

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 137 | 138 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation) |

Full rows: `../elements.csv`, class_id `136`.
