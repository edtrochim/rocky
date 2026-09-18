---
id: registry:L25:Dp
kind: class
title: Dp Stony desert - reg
system: registry:L25
code: Dp
name: Stony desert - reg
status: registered
decomposed: true
file_class_id: 2B5
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_CoarseMineralFragments
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_CoarseMineralFragments
  path: ../../../vocab/elements/LC_CoarseMineralFragments.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Dp Stony desert - reg

## Definition (verbatim, FAO LCLR)

This class is very basic, and generic being constituted by one mandatory stratum that defines the overall class structure. The strata are constituted by one basic element coarse fragment minerals.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2B6 | 2B7 Mandatory | `LC_CoarseMineralFragments` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `2B5`.
