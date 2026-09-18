---
id: registry:L31:Roa
kind: class
title: Roa Road
system: registry:L31
code: Roa
name: Road
status: registered
decomposed: true
file_class_id: '32'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_LinearSurface
links:
- rel: in_system
  id: registry:L31
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_LinearSurface
  path: ../../../vocab/elements/LC_LinearSurface.md
sources:
- okf/registry/_raw/L31/L31.lccs
schema: okf/0.1
---

# Roa Road

## Definition (verbatim, FAO LCLR)

It is an artificial surface with a linear configuration, located outside the urban perimeter, connecting one location to another, and through which people, animals or vehicles transit.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 33 | 34 Mandatory | `LC_LinearSurface` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `32`.
