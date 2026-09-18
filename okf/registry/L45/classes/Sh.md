---
id: registry:L45:Sh
kind: class
title: Sh Grass savanna
system: registry:L45
code: Sh
name: Grass savanna
status: registered
decomposed: true
file_class_id: '30'
n_rows: 31
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L45
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L45/L45.lccs
schema: okf/0.1
---

# Sh Grass savanna

## Definition (verbatim, FAO LCLR)

Lands with herbaceous types of cover. Tree and shrub cover is <4%.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 31 | 32 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 40.0–100.0 | height 80.0–300.0 | LC_VegetationArtificialityCharacteristic |
| 31 | 35 Optional | `LC_WoodyGrowthForm` | Mandatory | 1.0–4.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `30`.
