---
id: registry:L21:S
kind: class
title: S Sand
system: registry:L21
code: S
name: Sand
status: registered
decomposed: true
file_class_id: C0
n_rows: 26
rows_in: ../elements.csv
element_refs:
- LC_LooseAndShiftingSand
- LC_WaterBody
links:
- rel: in_system
  id: registry:L21
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_LooseAndShiftingSand
  path: ../../../vocab/elements/LC_LooseAndShiftingSand.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L21/L21.lccs
schema: okf/0.1
---

# S Sand

## Definition (verbatim, FAO LCLR)

In general, land of sand having thin soil or sand including deserts, dry salt flats, beaches, sand dunes.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| C1 | C2 Mandatory | `LC_LooseAndShiftingSand` | Mandatory | 50.0–100.0 |  |  |
| C1 | C2 Mandatory | `LC_WaterBody` | Optional | 50.0–100.0 | dynamics=Flowing; position=Above Surface | LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `C0`.
