---
id: registry:L35:G
kind: class
title: G Gravels, stones and/or boulders - river bank and rock debris
system: registry:L35
code: G
name: Gravels, stones and/or boulders - river bank and rock debris
status: registered
decomposed: true
file_class_id: 12A
n_rows: 25
rows_in: ../elements.csv
element_refs:
- LC_CoarseMineralFragments
links:
- rel: in_system
  id: registry:L35
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_CoarseMineralFragments
  path: ../../../vocab/elements/LC_CoarseMineralFragments.md
sources:
- okf/registry/_raw/L35/L35.lccs
schema: okf/0.1
---

# G Gravels, stones and/or boulders - river bank and rock debris

## Definition (verbatim, FAO LCLR)

NA

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 12B | 12C Mandatory | `LC_CoarseMineralFragments` | Mandatory |  | type=Gravel |  |
| 12B | 12C Mandatory | `LC_CoarseMineralFragments` | Optional |  | type=Stone |  |
| 12B | 12C Mandatory | `LC_CoarseMineralFragments` | Optional |  | type=Boulder |  |

Full rows: `../elements.csv`, class_id `12A`.
