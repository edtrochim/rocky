---
id: registry:L28:Other
kind: class
title: Other Other areas
system: registry:L28
code: Other
name: Other areas
status: registered
decomposed: true
file_class_id: AC
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_Building
- LC_BuiltUpSurface
links:
- rel: in_system
  id: registry:L28
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
- rel: uses_type
  id: element:LC_BuiltUpSurface
  path: ../../../vocab/elements/LC_BuiltUpSurface.md
sources:
- okf/registry/_raw/L28/L28.lccs
schema: okf/0.1
---

# Other Other areas

## Definition (verbatim, FAO LCLR)

Urban and rural built-up areas, air fields, infrastructure (power lines, railways, mining sites etc).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| AD | AE Mandatory | `LC_Building` | Mandatory |  |  |  |
| AD | B0 Mandatory | `LC_BuiltUpSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `AC`.
