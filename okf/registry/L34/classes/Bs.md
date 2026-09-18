---
id: registry:L34:Bs
kind: class
title: Bs Bare soil
system: registry:L34
code: Bs
name: Bare soil
status: registered
decomposed: true
file_class_id: '12'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
links:
- rel: in_system
  id: registry:L34
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
sources:
- okf/registry/_raw/L34/L34.lccs
schema: okf/0.1
---

# Bs Bare soil

## Definition (verbatim, FAO LCLR)

This land consists of bare soil which is not used for cultivation and usually devoid of grass and shrub cover.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 13 | 14 Mandatory | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `12`.
