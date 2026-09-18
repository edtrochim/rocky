---
id: registry:L8:SP
kind: class
title: SP Salt pans
system: registry:L8
code: SP
name: Salt pans
status: registered
decomposed: true
file_class_id: EC
n_rows: 15
rows_in: ../elements.csv
element_refs:
- LC_InorganicDeposits
links:
- rel: in_system
  id: registry:L8
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_InorganicDeposits
  path: ../../../vocab/elements/LC_InorganicDeposits.md
sources:
- okf/registry/_raw/L8/L8.lccs
schema: okf/0.1
---

# SP Salt pans

## Definition (verbatim, FAO LCLR)

Land used for salt production from seawater by solar evaporation

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| ED | EE Mandatory | `LC_InorganicDeposits` | Mandatory |  | type=Salt Flat |  |

Full rows: `../elements.csv`, class_id `EC`.
