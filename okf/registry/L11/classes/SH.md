---
id: registry:L11:SH
kind: class
title: SH Shrubland
system: registry:L11
code: SH
name: Shrubland
status: registered
decomposed: true
file_class_id: 14D
n_rows: 21
rows_in: ../elements.csv
element_refs:
- LC_BareRock
- LC_Shrub
links:
- rel: in_system
  id: registry:L11
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareRock
  path: ../../../vocab/elements/LC_BareRock.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L11/L11.lccs
schema: okf/0.1
---

# SH Shrubland

## Definition (verbatim, FAO LCLR)

Natural shrubs (H=0.5 to 1.5 m), occasionally with scattered rocks and boulders.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 14E | 14F Mandatory | `LC_Shrub` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 14E | 14F Mandatory | `LC_BareRock` | Optional |  |  |  |

Full rows: `../elements.csv`, class_id `14D`.
