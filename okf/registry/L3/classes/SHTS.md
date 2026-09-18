---
id: registry:L3:SHTS
kind: class
title: SHTS Shrubland
system: registry:L3
code: SHTS
name: Shrubland
status: registered
decomposed: true
file_class_id: A1
n_rows: 31
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L3
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L3/L3.lccs
schema: okf/0.1
---

# SHTS Shrubland

## Definition (verbatim, FAO LCLR)

Vegetation dominated by bushes; Natural shrubland vegetation, occasionally with sparse or closed herbaceous

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| A2 | 12A Mandatory | `LC_Tree` | Mandatory | 0.1–15.0 |  | LC_VegetationArtificialityCharacteristic |
| A2 | A3 Mandatory | `LC_Shrub` | Mandatory | 20.0–100.0 | height 0.5–1.5 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `A1`.
