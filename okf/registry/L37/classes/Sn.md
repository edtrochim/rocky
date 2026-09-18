---
id: registry:L37:Sn
kind: class
title: Sn Bare soil (eroded, denuded)
system: registry:L37
code: Sn
name: Bare soil (eroded, denuded)
status: registered
decomposed: true
file_class_id: '133'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
links:
- rel: in_system
  id: registry:L37
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
sources:
- okf/registry/_raw/L37/L37.LChS
schema: okf/0.1
---

# Sn Bare soil (eroded, denuded)

## Definition (verbatim, FAO LCLR)

Soils stripped of plant cover. Generally these soils are loose materials sensitive to erosion (stripping, ablation).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 134 | 135 Mandatory | `LC_BareSoil` | Mandatory | 0–100 |  |  |

Full rows: `../elements.csv`, class_id `133`.
