---
id: registry:L38:TOm
kind: class
title: TOm Open woody vegetation on mountain areas
system: registry:L38
code: TOm
name: Open woody vegetation on mountain areas
status: registered
decomposed: true
file_class_id: 2C1
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

# TOm Open woody vegetation on mountain areas

## Definition (verbatim, FAO LCLR)

Natural woodland open vegetation, occasionally with sparse or  closed  herbaceous coverage shrubs from closed to sparse/scattered with natural vegetation (shrub and herbaceous), above 2,500 m asl

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2C3 | 2C4 Mandatory | `LC_WoodyGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `2C1`.
