---
id: registry:L19:8WFP
kind: class
title: 8WFP River
system: registry:L19
code: 8WFP
name: River
status: registered
decomposed: true
file_class_id: D
n_rows: 24
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L19
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L19/L19.lccs
schema: okf/0.1
---

# 8WFP River

## Definition (verbatim, FAO LCLR)

Perennial Natural Waterbodies (Flowing).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| E | F Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Flowing; position=Above Surface | LC_WaterSalinityCharacteristic (type=Fresh); LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `D`.
