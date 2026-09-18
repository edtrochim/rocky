---
id: registry:L30:Hm
kind: class
title: Hm Hammada
system: registry:L30
code: Hm
name: Hammada
status: registered
decomposed: true
file_class_id: 19B
n_rows: 26
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_CoarseMineralFragments
links:
- rel: in_system
  id: registry:L30
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_CoarseMineralFragments
  path: ../../../vocab/elements/LC_CoarseMineralFragments.md
sources:
- okf/registry/_raw/L30/L30.lccs
schema: okf/0.1
---

# Hm Hammada

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 19D | 19E Mandatory | `LC_CoarseMineralFragments` | Mandatory |  | type=Stone |  |
| 19D | 1A0 Mandatory | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `19B`.
