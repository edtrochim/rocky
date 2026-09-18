---
id: registry:L15:SEEA-1
kind: class
title: SEEA 1 Artificial surfaces (including urban and associated areas)
system: registry:L15
code: SEEA 1
name: Artificial surfaces (including urban and associated areas)
status: registered
decomposed: true
file_class_id: '7'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_ArtificialSurfaceElement
links:
- rel: in_system
  id: registry:L15
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_ArtificialSurfaceElement
  path: ../../../vocab/elements/LC_ArtificialSurfaceElement.md
sources:
- okf/registry/_raw/L15/L15.lccs
schema: okf/0.1
---

# SEEA 1 Artificial surfaces (including urban and associated areas)

## Definition (verbatim, FAO LCLR)

The category is composed of any type of artificial surfaces

## Description

The class is composed of any type of areas with a predominant artificial surface. Any urban or related feature is included in this class, for example, urban parks (parks, parkland and laws). The class also includes industrial areas, and waste dump deposit and extraction sites.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 8 | 9 Mandatory | `LC_ArtificialSurfaceElement` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `7`.
