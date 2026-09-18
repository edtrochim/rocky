---
id: registry:L2:6GR
kind: class
title: 6GR Rock debris
system: registry:L2
code: 6GR
name: Rock debris
status: registered
decomposed: true
file_class_id: DA
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

# 6GR Rock debris

## Definition (verbatim, FAO LCLR)

River banks and rock debries

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| DB | DC Mandatory | `LC_BareRock` | Mandatory |  |  | LC_NaturalSurfaceCharacteristic |

Full rows: `../elements.csv`, class_id `DA`.
