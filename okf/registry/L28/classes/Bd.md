---
id: registry:L28:Bd
kind: class
title: Bd Bushland dense
system: registry:L28
code: Bd
name: Bushland dense
status: registered
decomposed: true
file_class_id: '41'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_Shrub
links:
- rel: in_system
  id: registry:L28
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L28/L28.lccs
schema: okf/0.1
---

# Bd Bushland dense

## Definition (verbatim, FAO LCLR)

Land not defined as "forest", spanning more than 0.5 ha with shrub height between 1-3 m and a cover of 40-100%. It does not include land that is predominantly under agricultural or urban land use.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 42 | 43 Mandatory | `LC_Shrub` | Mandatory | 40.0–100.0 | height 1.0–3.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `41`.
