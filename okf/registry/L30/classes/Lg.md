---
id: registry:L30:Lg
kind: class
title: Lg Lagoon
system: registry:L30
code: Lg
name: Lagoon
status: registered
decomposed: true
file_class_id: '166'
n_rows: 26
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L30
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L30/L30.lccs
schema: okf/0.1
---

# Lg Lagoon

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 168 | 169 Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Standing | LC_WaterSalinityCharacteristic (type=Brackish); LC_ArtificialityCharacteristic (type=Natural) |

Full rows: `../elements.csv`, class_id `166`.
