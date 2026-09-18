---
id: registry:L8:Ba
kind: class
title: Ba Baor
system: registry:L8
code: Ba
name: Baor
status: registered
decomposed: true
file_class_id: F5
n_rows: 27
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L8
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L8/L8.lccs
schema: okf/0.1
---

# Ba Baor

## Definition (verbatim, FAO LCLR)

Baor is a natural water body and a dead section of a river where it has changed its course. It normally is a part of the floodplain of the river to which inlets and outlets connect it.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| F6 | 2A6 Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Standing; position=Above Surface | LC_WaterSalinityCharacteristic (type=Fresh); LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `F5`.
