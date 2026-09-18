---
id: registry:L45:P
kind: class
title: P Beaches
system: registry:L45
code: P
name: Beaches
status: registered
decomposed: true
file_class_id: 8B
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_CoarseMineralFragments
- LC_LooseAndShiftingSand
links:
- rel: in_system
  id: registry:L45
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_CoarseMineralFragments
  path: ../../../vocab/elements/LC_CoarseMineralFragments.md
- rel: uses_type
  id: element:LC_LooseAndShiftingSand
  path: ../../../vocab/elements/LC_LooseAndShiftingSand.md
sources:
- okf/registry/_raw/L45/L45.lccs
schema: okf/0.1
---

# P Beaches

## Definition (verbatim, FAO LCLR)

Beach sand or shifting mounds of sand, formed by wind; active dunes.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 8C | 8D Mandatory | `LC_CoarseMineralFragments` | Mandatory |  |  |  |
| 8C | 8F Mandatory | `LC_LooseAndShiftingSand` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `8B`.
