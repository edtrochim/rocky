---
id: registry:L35:T
kind: class
title: T Tidal area
system: registry:L35
code: T
name: Tidal area
status: registered
decomposed: true
file_class_id: 14B
n_rows: 28
rows_in: ../elements.csv
element_refs:
- LC_LooseAndShiftingSand
- LC_WaterBody
links:
- rel: in_system
  id: registry:L35
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_LooseAndShiftingSand
  path: ../../../vocab/elements/LC_LooseAndShiftingSand.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L35/L35.lccs
schema: okf/0.1
---

# T Tidal area

## Definition (verbatim, FAO LCLR)

NA

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 14C | 14D Mandatory | `LC_WaterBody` | Mandatory |  | position=Above Surface; dynamics=Standing | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Saline) |
| 14C | 14D Mandatory | `LC_LooseAndShiftingSand` | Optional |  |  |  |

Full rows: `../elements.csv`, class_id `14B`.
