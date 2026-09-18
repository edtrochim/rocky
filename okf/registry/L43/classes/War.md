---
id: registry:L43:War
kind: class
title: War Mangroves (woody dominated aquatic areas)
system: registry:L43
code: War
name: Mangroves (woody dominated aquatic areas)
status: registered
decomposed: true
file_class_id: 4C
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L43
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L43/L43.lccs
schema: okf/0.1
---

# War Mangroves (woody dominated aquatic areas)

## Definition (verbatim, FAO LCLR)

Areas dominated by Mangroves i.e. coastal salt tolerant species.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4D | 51 Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Natural) |
| 4D | 4E Mandatory | `LC_WoodyGrowthForm` | Mandatory | 20.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `4C`.
