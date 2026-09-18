---
id: registry:L31:PWe
kind: class
title: PWe Permanent wetland
system: registry:L31
code: PWe
name: Permanent wetland
status: registered
decomposed: true
file_class_id: '93'
n_rows: 27
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L31
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L31/L31.lccs
schema: okf/0.1
---

# PWe Permanent wetland

## Definition (verbatim, FAO LCLR)

Areas where the soil is flooded by water all the year. Presence of vegetation can occur. In these areas occur, among others, riparian vegetation.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 94 | 95 Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Standing |  |
| 94 | 97 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 10.0–30.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `93`.
