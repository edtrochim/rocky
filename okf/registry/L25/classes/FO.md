---
id: registry:L25:FO
kind: class
title: FO Thicket
system: registry:L25
code: FO
name: Thicket
status: registered
decomposed: true
file_class_id: 9A
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

# FO Thicket

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of a thicket. It is constituted by one mandatory stratum that defines the overall class structure. The strata are constituted by one basic element shrubs.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 9B | 9C Mandatory | `LC_Shrub` | Mandatory | 70.0–100.0 | height 2.0–5.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `9A`.
