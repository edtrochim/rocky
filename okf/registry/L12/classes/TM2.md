---
id: registry:L12:TM2
kind: class
title: TM2 Trees, undifferentiated (open)
system: registry:L12
code: TM2
name: Trees, undifferentiated (open)
status: registered
decomposed: true
file_class_id: '107'
n_rows: 28
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# TM2 Trees, undifferentiated (open)

## Definition (verbatim, FAO LCLR)

Closed undifferentiated trees + herbaceous natural vegetation.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 108 | 109 Mandatory | `LC_Tree` | Mandatory | 20.0–60.0 |  | LC_VegetationArtificialityCharacteristic |
| 108 | 10C Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 20.0–100.0 |  |  |

Full rows: `../elements.csv`, class_id `107`.
