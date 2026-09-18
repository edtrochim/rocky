---
id: registry:L14:SS
kind: class
title: SS Saline soil
system: registry:L14
code: SS
name: Saline soil
status: registered
decomposed: true
file_class_id: DF
n_rows: 15
rows_in: ../elements.csv
element_refs:
- LC_InorganicDeposits
links:
- rel: in_system
  id: registry:L14
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_InorganicDeposits
  path: ../../../vocab/elements/LC_InorganicDeposits.md
sources:
- okf/registry/_raw/L14/L14.lccs
schema: okf/0.1
---

# SS Saline soil

## Definition (verbatim, FAO LCLR)

Expanse of ground covered with salt

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| E0 | E1 Mandatory | `LC_InorganicDeposits` | Mandatory |  | type=Salt Flat |  |

Full rows: `../elements.csv`, class_id `DF`.
