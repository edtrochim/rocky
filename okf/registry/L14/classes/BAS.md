---
id: registry:L14:BAS
kind: class
title: BAS Basaltic plain
system: registry:L14
code: BAS
name: Basaltic plain
status: registered
decomposed: true
file_class_id: C6
n_rows: 24
rows_in: ../elements.csv
element_refs:
- LC_CoarseMineralFragments
links:
- rel: in_system
  id: registry:L14
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_CoarseMineralFragments
  path: ../../../vocab/elements/LC_CoarseMineralFragments.md
sources:
- okf/registry/_raw/L14/L14.lccs
schema: okf/0.1
---

# BAS Basaltic plain

## Definition (verbatim, FAO LCLR)

Flat expanse of ground covered with Basaltic stones and gravels

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| C8 | C9 Mandatory | `LC_CoarseMineralFragments` | Mandatory |  | type=Stone |  |
| C8 | C9 Mandatory | `LC_CoarseMineralFragments` | Mandatory |  | type=Gravel |  |

Full rows: `../elements.csv`, class_id `C6`.
