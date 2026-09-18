---
id: registry:L18:VGS
kind: class
title: VGS Sparse natural vegetation
system: registry:L18
code: VGS
name: Sparse natural vegetation
status: registered
decomposed: true
file_class_id: 4F
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L18
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L18/L18.lccs
schema: okf/0.1
---

# VGS Sparse natural vegetation

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 50 | 51 Mandatory | `LC_WoodyGrowthForm` | Mandatory | 20.0–40.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `4F`.
