---
id: registry:L7:Ido
kind: class
title: Ido Industial and Other
system: registry:L7
code: Ido
name: Industial and Other
status: registered
decomposed: true
file_class_id: B9
n_rows: 28
rows_in: ../elements.csv
element_refs:
- LC_OtherArtificialSurface
- LC_OtherConstruction
links:
- rel: in_system
  id: registry:L7
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_OtherArtificialSurface
  path: ../../../vocab/elements/LC_OtherArtificialSurface.md
- rel: uses_type
  id: element:LC_OtherConstruction
  path: ../../../vocab/elements/LC_OtherConstruction.md
sources:
- okf/registry/_raw/L7/L7.lccs
schema: okf/0.1
---

# Ido Industial and Other

## Definition (verbatim, FAO LCLR)

Zones designated for industrial use, with facilities for manufacturing or production.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| BA | BB Mandatory | `LC_OtherConstruction` | Mandatory |  |  | LC_ConstructionUse (type=Industrial) |
| BE | BF Mandatory | `LC_OtherArtificialSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `B9`.
