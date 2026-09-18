---
id: registry:L31:BSo
kind: class
title: BSo Bare soil
system: registry:L31
code: BSo
name: Bare soil
status: registered
decomposed: true
file_class_id: 2E
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
links:
- rel: in_system
  id: registry:L31
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
sources:
- okf/registry/_raw/L31/L31.lccs
schema: okf/0.1
---

# BSo Bare soil

## Definition (verbatim, FAO LCLR)

Portion of land that is not covered by any biotic or abiotic material, because of fire, deforestation or other human interventions. The land may show regrowth of natural vegetation after the interventions.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2F | 30 Mandatory | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `2E`.
