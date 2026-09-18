---
id: registry:L37:Savher
kind: class
title: Savher Grassy Savanna
system: registry:L37
code: Savher
name: Grassy Savanna
status: registered
decomposed: true
file_class_id: '120'
n_rows: 26
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L37
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L37/L37.LChS
schema: okf/0.1
---

# Savher Grassy Savanna

## Definition (verbatim, FAO LCLR)

They are areas where trees and shrubs are usually absent (coverage less than 10%). Grassy formations include a continuous grass layer at least 80 cm high.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 121 | 122 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 0–90 | height 80–300 | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural or Seminatural) |
| 121 | 125 Mandatory | `LC_WoodyGrowthForm` | Mandatory | 0–10 |  | LC_VegetationArtificialityCharacteristic (vegetationArtificiality=Natural or Seminatural) |

Full rows: `../elements.csv`, class_id `120`.
