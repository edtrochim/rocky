---
id: registry:L41:Hn
kind: class
title: Hn Aquatic Herbs dominated areas
system: registry:L41
code: Hn
name: Aquatic Herbs dominated areas
status: registered
decomposed: true
file_class_id: 4D
n_rows: 35
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L41
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L41/L41.lccs
schema: okf/0.1
---

# Hn Aquatic Herbs dominated areas

## Definition (verbatim, FAO LCLR)

Wetlands or floodplains with dominant herbaceous vegetation, such as reeds, sedges, or other hydrophilic plants.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4E | 52 Optional | `LC_WaterBody` | Mandatory |  | position=Above Surface | LC_WaterSalinityCharacteristic (type=Fresh); LC_ArtificialityCharacteristic (type=Natural) |
| 4E | 4F Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 20.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `4D`.
