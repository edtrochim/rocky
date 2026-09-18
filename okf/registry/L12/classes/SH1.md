---
id: registry:L12:SH1
kind: class
title: SH1 Shrubland (closed)
system: registry:L12
code: SH1
name: Shrubland (closed)
status: registered
decomposed: true
file_class_id: A1
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_Shrub
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# SH1 Shrubland (closed)

## Definition (verbatim, FAO LCLR)

Closed natural shrubs (H=0.5 to 1.5m), commonly observed on river valley slopes, ocassionally with scattered rocks and boulders.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| A2 | A3 Mandatory | `LC_Shrub` | Mandatory | 60.0–100.0 | height 0.5–1.5 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `A1`.
