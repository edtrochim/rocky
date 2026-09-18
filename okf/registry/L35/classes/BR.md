---
id: registry:L35:BR
kind: class
title: BR Bare soil
system: registry:L35
code: BR
name: Bare soil
status: registered
decomposed: true
file_class_id: '130'
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_BareRock
- LC_CoarseMineralFragments
links:
- rel: in_system
  id: registry:L35
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareRock
  path: ../../../vocab/elements/LC_BareRock.md
- rel: uses_type
  id: element:LC_CoarseMineralFragments
  path: ../../../vocab/elements/LC_CoarseMineralFragments.md
sources:
- okf/registry/_raw/L35/L35.lccs
schema: okf/0.1
---

# BR Bare soil

## Definition (verbatim, FAO LCLR)

NA

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 131 | 132 Mandatory | `LC_BareRock` | Mandatory |  |  |  |
| 131 | 132 Mandatory | `LC_CoarseMineralFragments` | Optional |  |  |  |

Full rows: `../elements.csv`, class_id `130`.
