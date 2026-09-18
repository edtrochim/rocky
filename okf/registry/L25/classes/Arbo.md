---
id: registry:L25:Arbo
kind: class
title: Arbo Open low shrublands
system: registry:L25
code: Arbo
name: Open low shrublands
status: registered
decomposed: true
file_class_id: B4
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

# Arbo Open low shrublands

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of a open low shrublands. It is constituted by one mandatory stratum that defines the overall class structure. The strata are constituted by one basic element shrubs (cover: 20-70%).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| B5 | B6 Mandatory | `LC_Shrub` | Mandatory | 20.0–70.0 | height 0.3–2.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `B4`.
