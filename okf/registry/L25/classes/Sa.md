---
id: registry:L25:Sa
kind: class
title: Sa Tree savanna
system: registry:L25
code: Sa
name: Tree savanna
status: registered
decomposed: true
file_class_id: D6
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Sa Tree savanna

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of tree savanna. It is constituted by one mandatory horizontal pattern that defines the overall class structure. The strata is constituted by one basic element herbaceous growth forms.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| D7 | D8 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 40.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| D7 | DB Mandatory | `LC_Tree` | Mandatory | 4.0–20.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `D6`.
