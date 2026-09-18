---
id: registry:L21:G
kind: class
title: G Grassland
system: registry:L21
code: G
name: Grassland
status: registered
decomposed: true
file_class_id: '59'
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L21
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L21/L21.lccs
schema: okf/0.1
---

# G Grassland

## Definition (verbatim, FAO LCLR)

Grasslands are characterized as lands dominated by grasses rather than large shrubs or trees. It is crucial that the rainfall is concentrated in six or eight months of the year, followed by a long period of drought when fires can occur.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 5A | 5B Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 15.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `59`.
