---
id: registry:L38:TO
kind: class
title: TO Open woody vegetation
system: registry:L38
code: TO
name: Open woody vegetation
status: registered
decomposed: true
file_class_id: '106'
n_rows: 18
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

# TO Open woody vegetation

## Definition (verbatim, FAO LCLR)

Natural woodland open vegetation, occasionally with sparse or  closed  herbaceous coverage shrubs from closed to sparse/scattered with natural vegetation (shrub and herbaceous)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 107 | 108 Mandatory | `LC_WoodyGrowthForm` | Mandatory | 10.0–40.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `106`.
