---
id: registry:L25:Fco
kind: class
title: Fco Woodland (open)
system: registry:L25
code: Fco
name: Woodland (open)
status: registered
decomposed: true
file_class_id: '71'
n_rows: 57
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Fco Woodland (open)

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of a so-called open woodland area. It is constituted by one mandatory stratum that defines the overall class structure. The strata are constituted by one basic element tree.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 72 | 73 Optional | `LC_Tree` | Mandatory | 10.0–25.0 | height 20.0–30.0 | LC_VegetationArtificialityCharacteristic |
| 72 | 76 Mandatory | `LC_Tree` | Mandatory | 20.0–70.0 | height 6.0–20.0 | LC_VegetationArtificialityCharacteristic |
| 72 | 79 Optional | `LC_Shrub` | Mandatory | 2.0–10.0 | height 3.0–5.0 | LC_VegetationArtificialityCharacteristic |
| 72 | 7C Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 20.0–70.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `71`.
