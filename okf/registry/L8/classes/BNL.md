---
id: registry:L8:BNL
kind: class
title: BNL Built-up non-linear
system: registry:L8
code: BNL
name: Built-up non-linear
status: registered
decomposed: true
file_class_id: DF
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_NonLinearSurface
links:
- rel: in_system
  id: registry:L8
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_NonLinearSurface
  path: ../../../vocab/elements/LC_NonLinearSurface.md
sources:
- okf/registry/_raw/L8/L8.lccs
schema: okf/0.1
---

# BNL Built-up non-linear

## Definition (verbatim, FAO LCLR)

This category describes built-up areas where non-linear artificial constructions cover the land with an impervious surface.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| E0 | E1 Mandatory | `LC_NonLinearSurface` | Mandatory |  | construction_material=Hard Material | LC_ConstructionUse (type=Urban Residential Area, Industrial Area, Commercial Area,) |

Full rows: `../elements.csv`, class_id `DF`.
