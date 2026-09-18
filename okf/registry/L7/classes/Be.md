---
id: registry:L7:Be
kind: class
title: Be Beaches
system: registry:L7
code: Be
name: Beaches
status: registered
decomposed: true
file_class_id: '98'
n_rows: 21
rows_in: ../elements.csv
element_refs:
- LC_CoarseMineralFragments
- LC_LooseAndShiftingSand
links:
- rel: in_system
  id: registry:L7
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_CoarseMineralFragments
  path: ../../../vocab/elements/LC_CoarseMineralFragments.md
- rel: uses_type
  id: element:LC_LooseAndShiftingSand
  path: ../../../vocab/elements/LC_LooseAndShiftingSand.md
sources:
- okf/registry/_raw/L7/L7.lccs
schema: okf/0.1
---

# Be Beaches

## Definition (verbatim, FAO LCLR)

Strip of natural land that lies along the coast and usually consists of loose particles, which are composed of sand.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 9A | 9B Mandatory | `LC_LooseAndShiftingSand` | Exclusive |  |  |  |
| 9A | 9B Mandatory | `LC_CoarseMineralFragments` | Exclusive |  |  |  |

Full rows: `../elements.csv`, class_id `98`.
