---
id: registry:L49:Sn
kind: class
title: Sn Bare surfaces
system: registry:L49
code: Sn
name: Bare surfaces
status: registered
decomposed: true
file_class_id: '22'
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_NaturalSurfaceElement
links:
- rel: in_system
  id: registry:L49
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_NaturalSurfaceElement
  path: ../../../vocab/elements/LC_NaturalSurfaceElement.md
sources:
- okf/registry/_raw/L49/L49.LChS
schema: okf/0.1
---

# Sn Bare surfaces

## Definition (verbatim, FAO LCLR)

This class represents land surfaces with little to no plant cover. These areas may be characterized by aeolian deposits, sand dunes, bare soil, salt crusts, or beach zones. In some cases, the absence of vegetation may be caused by overgrazing, severe wind or water erosion, or by the presence of extraction activities, unpaved roads, or other infrastructure (Di Gregorio et al., 2022; FAO, 2020). It is expressed as follows: • One stratum of natural surfaces. •Presence type: fixed.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 25 | 34 Fixed | `LC_NaturalSurfaceElement` | Fixed | 0–100 | height 0–200; depth -100–0; density 0–999; lengthOfTemporalRelationship 1–100 |  |

Full rows: `../elements.csv`, class_id `22`.
