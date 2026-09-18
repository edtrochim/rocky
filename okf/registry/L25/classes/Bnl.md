---
id: registry:L25:Bnl
kind: class
title: Bnl Builtup - non-linear
system: registry:L25
code: Bnl
name: Builtup - non-linear
status: registered
decomposed: true
file_class_id: 2DF
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_NonLinearSurface
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_NonLinearSurface
  path: ../../../vocab/elements/LC_NonLinearSurface.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Bnl Builtup - non-linear

## Definition (verbatim, FAO LCLR)

It corresponds to artificial and impervious surface which are paved with hard materials are built-up non-linear. The presence of sub-surfaces is recognized with types of artificial surface.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2E0 | 2E1 Mandatory | `LC_NonLinearSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `2DF`.
