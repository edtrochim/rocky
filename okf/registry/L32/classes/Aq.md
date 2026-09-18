---
id: registry:L32:Aq
kind: class
title: Aq Aquaculture
system: registry:L32
code: Aq
name: Aquaculture
status: registered
decomposed: true
file_class_id: '43'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L32
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L32/L32.lccs
schema: okf/0.1
---

# Aq Aquaculture

## Definition (verbatim, FAO LCLR)

Aquaculture area with standing and freshwater.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 44 | 45 Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Standing | LC_AquacultureCharacteristic (type=Freshwater) |

Full rows: `../elements.csv`, class_id `43`.
