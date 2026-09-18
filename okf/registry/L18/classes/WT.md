---
id: registry:L18:WT
kind: class
title: WT Water bodies
system: registry:L18
code: WT
name: Water bodies
status: registered
decomposed: true
file_class_id: 5C
n_rows: 31
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L18
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L18/L18.lccs
schema: okf/0.1
---

# WT Water bodies

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 5D | 5E Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Flowing | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Fresh) |
| 5D | 7C Optional | `LC_HerbaceousGrowthForm` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `5C`.
