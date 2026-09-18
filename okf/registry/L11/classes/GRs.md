---
id: registry:L11:GRs
kind: class
title: GRs Sparse grassland
system: registry:L11
code: GRs
name: Sparse grassland
status: registered
decomposed: true
file_class_id: 15D
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_BareRock
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L11
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareRock
  path: ../../../vocab/elements/LC_BareRock.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L11/L11.lccs
schema: okf/0.1
---

# GRs Sparse grassland

## Definition (verbatim, FAO LCLR)

Degraded grassland with low vegetative cover, occasionally bare with scattered rock outcrops.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 15E | 15F Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 0.0–20.0 |  | LC_VegetationArtificialityCharacteristic |
| 15E | 15F Mandatory | `LC_BareRock` | Optional |  |  |  |

Full rows: `../elements.csv`, class_id `15D`.
