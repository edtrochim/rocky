---
id: registry:L31:Lak
kind: class
title: Lak Lake
system: registry:L31
code: Lak
name: Lake
status: registered
decomposed: true
file_class_id: 8D
n_rows: 23
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L31
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L31/L31.lccs
schema: okf/0.1
---

# Lak Lake

## Definition (verbatim, FAO LCLR)

Permanent water body surrounded by land. Generally found in areas with rivers and ongoing flooding.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 8E | 8F Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Standing | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `8D`.
