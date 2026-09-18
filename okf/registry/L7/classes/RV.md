---
id: registry:L7:RV
kind: class
title: RV Rural Villages
system: registry:L7
code: RV
name: Rural Villages
status: registered
decomposed: true
file_class_id: B1
n_rows: 27
rows_in: ../elements.csv
element_refs:
- LC_Building
- LC_OtherArtificialSurface
links:
- rel: in_system
  id: registry:L7
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
- rel: uses_type
  id: element:LC_OtherArtificialSurface
  path: ../../../vocab/elements/LC_OtherArtificialSurface.md
sources:
- okf/registry/_raw/L7/L7.lccs
schema: okf/0.1
---

# RV Rural Villages

## Definition (verbatim, FAO LCLR)

Geographic areas of clustered or linear rural dwelling covered by fruit trees and other plantation.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| B3 | B4 Mandatory | `LC_Building` | Mandatory |  |  |  |
| B6 | B7 Mandatory | `LC_OtherArtificialSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `B1`.
