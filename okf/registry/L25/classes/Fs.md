---
id: registry:L25:Fs
kind: class
title: Fs Dry forest
system: registry:L25
code: Fs
name: Dry forest
status: registered
decomposed: true
file_class_id: '62'
n_rows: 29
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Fs Dry forest

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of a so-called dry forest. It is constituted by one mandatory stratum that defines the overall class structure. The strata is constituted by one basic element tree.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 63 | 64 Mandatory | `LC_Tree` | Mandatory | 70.0–100.0 | height 8.0–30.0 |  |
| 63 | 66 Mandatory | `LC_Shrub` | Mandatory | 10.0–50.0 | height 4.0–5.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `62`.
