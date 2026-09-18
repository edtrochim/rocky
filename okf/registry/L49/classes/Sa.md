---
id: registry:L49:Sa
kind: class
title: Sa Artificial surfaces
system: registry:L49
code: Sa
name: Artificial surfaces
status: registered
decomposed: true
file_class_id: '21'
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_ArtificialSurfaceElement
links:
- rel: in_system
  id: registry:L49
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_ArtificialSurfaceElement
  path: ../../../vocab/elements/LC_ArtificialSurfaceElement.md
sources:
- okf/registry/_raw/L49/L49.LChS
schema: okf/0.1
---

# Sa Artificial surfaces

## Definition (verbatim, FAO LCLR)

This land cover class is characterized by the presence of built-up areas. Usually, the original natural cover has been permanently replaced by impermeable or semi-permeable materials. These include urban and rural built-up areas, transportation infrastructure, industrial complexes, and sites for extraction or waste disposal. Built-up non-linear features typically correspond to compacted or paved surfaces with hard materials (FAO, 2020). It is expressed as follows: •Element of artificial surface. •Presence type: fixed.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 24 | 33 Fixed | `LC_ArtificialSurfaceElement` | Fixed | 0–100 | height 0–200; depth -100–0; density 0–999; lengthOfTemporalRelationship 1–100 |  |

Full rows: `../elements.csv`, class_id `21`.
