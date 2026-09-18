---
id: registry:L4:GL
kind: class
title: GL Grassland
system: registry:L4
code: GL
name: Grassland
status: registered
decomposed: true
file_class_id: '39'
n_rows: 17
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L4
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L4/L4.lccs
schema: okf/0.1
---

# GL Grassland

## Definition (verbatim, FAO LCLR)

Grassland dominated by herbaous growth forms.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3A | 3B Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `39`.
