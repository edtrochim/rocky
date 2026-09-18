---
id: registry:L25:Tr
kind: class
title: Tr Rocks, coarse fragments
system: registry:L25
code: Tr
name: Rocks, coarse fragments
status: registered
decomposed: true
file_class_id: 2A8
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_CoarseMineralFragments
- LC_RocksSurfaceElement
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_CoarseMineralFragments
  path: ../../../vocab/elements/LC_CoarseMineralFragments.md
- rel: uses_type
  id: element:LC_RocksSurfaceElement
  path: ../../../vocab/elements/LC_RocksSurfaceElement.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Tr Rocks, coarse fragments

## Definition (verbatim, FAO LCLR)

It corresponds to areas with natural surfaces where the rocky and coarse fragments are dominant. The presence of sub-surfaces is recognized with main physiognomic aspect.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2A9 | 2AA Mandatory | `LC_RocksSurfaceElement` | Exclusive |  |  |  |
| 2A9 | 2AA Mandatory | `LC_CoarseMineralFragments` | Exclusive |  |  |  |

Full rows: `../elements.csv`, class_id `2A8`.
