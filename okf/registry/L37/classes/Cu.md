---
id: registry:L37:Cu
kind: class
title: Cu Crusty soil
system: registry:L37
code: Cu
name: Crusty soil
status: registered
decomposed: true
file_class_id: '137'
n_rows: 16
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_CoarseMineralFragments
links:
- rel: in_system
  id: registry:L37
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_CoarseMineralFragments
  path: ../../../vocab/elements/LC_CoarseMineralFragments.md
sources:
- okf/registry/_raw/L37/L37.LChS
schema: okf/0.1
---

# Cu Crusty soil

## Definition (verbatim, FAO LCLR)

Highly consolidated surface formation resulting from the accumulation of sesquioxides of iron, alumina, or even manganese, common in the tropical zone, where it restricts the agricultural domain. In general, these soils are devoid of plant cover. The grass layer is dominant.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 138 | 139 Mandatory | `LC_BareSoil` | Mandatory |  |  |  |
| 138 | 139 Mandatory | `LC_CoarseMineralFragments` | Optional |  |  |  |

Full rows: `../elements.csv`, class_id `137`.
