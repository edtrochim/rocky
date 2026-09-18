---
id: registry:L25:Abm-h
kind: class
title: Abm/h Shrubland (medium , high)
system: registry:L25
code: Abm/h
name: Shrubland (medium , high)
status: registered
decomposed: true
file_class_id: '95'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_Shrub
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Abm/h Shrubland (medium , high)

## Definition (verbatim, FAO LCLR)

This class is constituted mainly by shrubs with a coverage of about 20% to 100%. Vegetation height varies between 2m and 5m.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 96 | 97 Mandatory | `LC_Shrub` | Mandatory | 20.0–100.0 | height 2.0–5.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `95`.
