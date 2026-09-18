---
id: registry:L45:Ml
kind: class
title: Ml Mangrove forest
system: registry:L45
code: Ml
name: Mangrove forest
status: registered
decomposed: true
file_class_id: '38'
n_rows: 34
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L45
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L45/L45.lccs
schema: okf/0.1
---

# Ml Mangrove forest

## Definition (verbatim, FAO LCLR)

Coastal forests of stilted shrubs or trees bordering the ocean or coastal estuaries, composed of one or several mangroves species.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 39 | 3A Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_WaterSalinityCharacteristic (type=Brackish); LC_ArtificialityCharacteristic (type=Natural) |
| 39 | 3E Mandatory | `LC_WoodyGrowthForm` | Mandatory | 20.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `38`.
