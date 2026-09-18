---
id: registry:L28:FL
kind: class
title: FL Forest lowland
system: registry:L28
code: FL
name: Forest lowland
status: registered
decomposed: true
file_class_id: D
n_rows: 20
rows_in: ../elements.csv
element_refs:
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L28
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L28/L28.lccs
schema: okf/0.1
---

# FL Forest lowland

## Definition (verbatim, FAO LCLR)

Woody growth form with the geographical aspect of groundwater forests and some coastal forests, < 800 m asl.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| F | 10 Mandatory | `LC_WoodyGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `D`.
