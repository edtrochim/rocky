---
id: registry:L14:OW
kind: class
title: OW Sparse to very open woody vegetation
system: registry:L14
code: OW
name: Sparse to very open woody vegetation
status: registered
decomposed: true
file_class_id: '47'
n_rows: 29
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L14
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L14/L14.lccs
schema: okf/0.1
---

# OW Sparse to very open woody vegetation

## Definition (verbatim, FAO LCLR)

Open woody vegetation (5-40 %) + Natural Herbaceous vegetation

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 48 | 49 Mandatory | `LC_WoodyGrowthForm` | Mandatory | 5.0–40.0 |  | LC_VegetationArtificialityCharacteristic |
| 48 | F9 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `47`.
