---
id: registry:L5:SWE
kind: class
title: SWE Shrubs in temporary wet soil
system: registry:L5
code: SWE
name: Shrubs in temporary wet soil
status: registered
decomposed: true
file_class_id: 5C
n_rows: 25
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_WaterBody
links:
- rel: in_system
  id: registry:L5
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L5/L5.lccs
schema: okf/0.1
---

# SWE Shrubs in temporary wet soil

## Definition (verbatim, FAO LCLR)

This class includes areas mainly covered by shrubs of-ten with herbaceous vegeta-tion, usually flooded or liable to flooding by fresh, stagnant or circulating water.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 5D | 61 Mandatory | `LC_WaterBody` | Mandatory |  |  |  |
| 5D | 5E Mandatory | `LC_Shrub` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `5C`.
