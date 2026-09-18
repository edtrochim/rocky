---
id: registry:L11:TM
kind: class
title: TM Trees mixed
system: registry:L11
code: TM
name: Trees mixed
status: registered
decomposed: true
file_class_id: FF
n_rows: 25
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L11
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L11/L11.lccs
schema: okf/0.1
---

# TM Trees mixed

## Definition (verbatim, FAO LCLR)

Undifferentiated trees, where neither needle-leaved nor broad-leaved dominate (20%-100% coverage where single specie is below 75%).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 100 | 101 Mandatory | `LC_Tree` | Mandatory | 20.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 100 | 101 Mandatory | `LC_HerbaceousGrowthForm` | Optional |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `FF`.
