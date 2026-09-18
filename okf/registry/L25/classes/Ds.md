---
id: registry:L25:Ds
kind: class
title: Ds Salt deposit
system: registry:L25
code: Ds
name: Salt deposit
status: registered
decomposed: true
file_class_id: 2D1
n_rows: 15
rows_in: ../elements.csv
element_refs:
- LC_InorganicDeposits
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_InorganicDeposits
  path: ../../../vocab/elements/LC_InorganicDeposits.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Ds Salt deposit

## Definition (verbatim, FAO LCLR)

This class is very basic, and generic being constituted by one mandatory stratum that defines overall class structure. The strata are constituted by one basic element inorganic deposit with salt flat type.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2D2 | 2D3 Mandatory | `LC_InorganicDeposits` | Mandatory |  | type=Salt Flat |  |

Full rows: `../elements.csv`, class_id `2D1`.
