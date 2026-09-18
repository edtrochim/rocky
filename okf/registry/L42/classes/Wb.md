---
id: registry:L42:Wb
kind: class
title: Wb Water bodies
system: registry:L42
code: Wb
name: Water bodies
status: registered
decomposed: true
file_class_id: '24'
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L42
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L42/L42.lccs
schema: okf/0.1
---

# Wb Water bodies

## Definition (verbatim, FAO LCLR)

The water surface includes inland aquatic areas and marine aquatic areas.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 25 | 26 Mandatory | `LC_WaterBody` | Mandatory |  |  | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `24`.
