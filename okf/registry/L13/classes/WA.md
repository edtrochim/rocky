---
id: registry:L13:WA
kind: class
title: WA Artificial Waterbodies
system: registry:L13
code: WA
name: Artificial Waterbodies
status: registered
decomposed: true
file_class_id: '74'
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L13
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L13/L13.lccs
schema: okf/0.1
---

# WA Artificial Waterbodies

## Definition (verbatim, FAO LCLR)

An artificially-created body of water, by damming a source. Often used for flood control, as a drinking water supply (reservoir), recreation, ornamentation (artificial pond), or other purpose or combination of purposes.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 75 | 76 Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Artificial) |

Full rows: `../elements.csv`, class_id `74`.
