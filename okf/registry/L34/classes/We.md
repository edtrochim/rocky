---
id: registry:L34:We
kind: class
title: We Wetland
system: registry:L34
code: We
name: Wetland
status: registered
decomposed: true
file_class_id: 3B
n_rows: 29
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L34
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L34/L34.lccs
schema: okf/0.1
---

# We Wetland

## Definition (verbatim, FAO LCLR)

This class consists of swamp and wetland areas in which herbaceous or aquaic vegetation are present. It may include pemanent or semi permanent wetland.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3C | 40 Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Natural) |
| 3C | 3D Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `3B`.
