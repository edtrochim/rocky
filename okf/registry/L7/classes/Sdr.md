---
id: registry:L7:Sdr
kind: class
title: Sdr Stony desert
system: registry:L7
code: Sdr
name: Stony desert
status: registered
decomposed: true
file_class_id: 8C
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_CoarseMineralFragments
links:
- rel: in_system
  id: registry:L7
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_CoarseMineralFragments
  path: ../../../vocab/elements/LC_CoarseMineralFragments.md
sources:
- okf/registry/_raw/L7/L7.lccs
schema: okf/0.1
---

# Sdr Stony desert

## Definition (verbatim, FAO LCLR)

Lands with exposed unconsolidated rocks, that and never have more than 4% vegetated cover during any time of the year.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 8D | 8E Mandatory | `LC_CoarseMineralFragments` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `8C`.
