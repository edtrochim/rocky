---
id: registry:L28:Fm
kind: class
title: Fm Forest mangrove
system: registry:L28
code: Fm
name: Forest mangrove
status: registered
decomposed: true
file_class_id: '13'
n_rows: 41
rows_in: ../elements.csv
element_refs:
- LC_Tree
- LC_WaterBody
links:
- rel: in_system
  id: registry:L28
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L28/L28.lccs
schema: okf/0.1
---

# Fm Forest mangrove

## Definition (verbatim, FAO LCLR)

Area of forest and other wooded land with mangrove vegetation along coastal areas

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 16 | 17 Mandatory | `LC_Tree` | Mandatory | 10.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 16 | 1A Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Flowing | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Brackish) |

Full rows: `../elements.csv`, class_id `13`.
