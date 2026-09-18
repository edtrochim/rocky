---
id: registry:L4:BS
kind: class
title: BS Bare surfaces
system: registry:L4
code: BS
name: Bare surfaces
status: registered
decomposed: true
file_class_id: '43'
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_LinearSurface
- LC_NonBuiltUpSurface
- LC_SoilSandDepositsSurfaceElement
links:
- rel: in_system
  id: registry:L4
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_LinearSurface
  path: ../../../vocab/elements/LC_LinearSurface.md
- rel: uses_type
  id: element:LC_NonBuiltUpSurface
  path: ../../../vocab/elements/LC_NonBuiltUpSurface.md
- rel: uses_type
  id: element:LC_SoilSandDepositsSurfaceElement
  path: ../../../vocab/elements/LC_SoilSandDepositsSurfaceElement.md
sources:
- okf/registry/_raw/L4/L4.lccs
schema: okf/0.1
---

# BS Bare surfaces

## Definition (verbatim, FAO LCLR)

Bare surfaces dominated by bare soil and non-built up areas.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 44 | 45 Mandatory | `LC_LinearSurface` | Mandatory |  |  |  |
| 44 | 60 Mandatory | `LC_SoilSandDepositsSurfaceElement` | Mandatory |  |  |  |
| 44 | 63 Mandatory | `LC_NonBuiltUpSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `43`.
