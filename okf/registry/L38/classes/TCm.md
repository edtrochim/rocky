---
id: registry:L38:TCm
kind: class
title: TCm Closed woody vegetation on mountain areas
system: registry:L38
code: TCm
name: Closed woody vegetation on mountain areas
status: registered
decomposed: true
file_class_id: 2C7
n_rows: 20
rows_in: ../elements.csv
element_refs:
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L38
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L38/L38.lccs
schema: okf/0.1
---

# TCm Closed woody vegetation on mountain areas

## Definition (verbatim, FAO LCLR)

Undifferentiated natural closed trees above 2,500 m asl

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2C9 | 2CA Mandatory | `LC_WoodyGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `2C7`.
