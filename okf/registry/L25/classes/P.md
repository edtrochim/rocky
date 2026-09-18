---
id: registry:L25:P
kind: class
title: P Beaches
system: registry:L25
code: P
name: Beaches
status: registered
decomposed: true
file_class_id: 2D9
n_rows: 21
rows_in: ../elements.csv
element_refs:
- LC_CoarseMineralFragments
- LC_LooseAndShiftingSand
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_CoarseMineralFragments
  path: ../../../vocab/elements/LC_CoarseMineralFragments.md
- rel: uses_type
  id: element:LC_LooseAndShiftingSand
  path: ../../../vocab/elements/LC_LooseAndShiftingSand.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# P Beaches

## Definition (verbatim, FAO LCLR)

This class is very basic, and generic being constituted by one mandatory stratum that defines overall class structure. The strata are constituted by one basic element lose and shifting sand.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2DB | 2DC Mandatory | `LC_LooseAndShiftingSand` | Exclusive |  |  |  |
| 2DB | 2DC Mandatory | `LC_CoarseMineralFragments` | Exclusive |  |  |  |

Full rows: `../elements.csv`, class_id `2D9`.
