---
id: registry:L14:SD
kind: class
title: SD Sandy areas
system: registry:L14
code: SD
name: Sandy areas
status: registered
decomposed: true
file_class_id: D7
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_LooseAndShiftingSand
links:
- rel: in_system
  id: registry:L14
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_LooseAndShiftingSand
  path: ../../../vocab/elements/LC_LooseAndShiftingSand.md
sources:
- okf/registry/_raw/L14/L14.lccs
schema: okf/0.1
---

# SD Sandy areas

## Definition (verbatim, FAO LCLR)

Shifting and loosing sand not covered by vegetation and if present is negligible

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| D8 | D9 Mandatory | `LC_LooseAndShiftingSand` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `D7`.
