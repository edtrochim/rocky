---
id: registry:L20:He_in
kind: class
title: He_in Parmenently flooded grassland
system: registry:L20
code: He_in
name: Parmenently flooded grassland
status: registered
decomposed: true
file_class_id: '95'
n_rows: 33
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L20
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L20/L20.lccs
schema: okf/0.1
---

# He_in Parmenently flooded grassland

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 96 | 97 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 15.0–100.0 | height 0.0–150.0 |  |
| 96 | 99 Mandatory | `LC_WaterBody` | Mandatory |  | position=Above Surface | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `95`.
