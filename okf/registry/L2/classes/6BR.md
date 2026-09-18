---
id: registry:L2:6BR
kind: class
title: 6BR Bare rock
system: registry:L2
code: 6BR
name: Bare rock
status: registered
decomposed: true
file_class_id: D0
n_rows: 17
rows_in: ../elements.csv
element_refs:
- LC_BareRock
links:
- rel: in_system
  id: registry:L2
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareRock
  path: ../../../vocab/elements/LC_BareRock.md
sources:
- okf/registry/_raw/L2/L2.lccs
schema: okf/0.1
---

# 6BR Bare rock

## Definition (verbatim, FAO LCLR)

Bare rock

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| D1 | D2 Mandatory | `LC_BareRock` | Mandatory |  |  | LC_NaturalSurfaceCharacteristic |

Full rows: `../elements.csv`, class_id `D0`.
