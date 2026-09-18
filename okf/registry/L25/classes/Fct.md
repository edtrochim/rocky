---
id: registry:L25:Fct
kind: class
title: Fct Woodland (very open) - wooded land savanna
system: registry:L25
code: Fct
name: Woodland (very open) - wooded land savanna
status: registered
decomposed: true
file_class_id: 7F
n_rows: 45
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

# Fct Woodland (very open) - wooded land savanna

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of a so-called very open woodland area. It is constituted by one mandatory stratum that defines the overall class structure.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 80 | 81 Mandatory | `LC_Tree` | Mandatory | 20.0–40.0 | height 6.0–15.0 | LC_VegetationArtificialityCharacteristic |
| 80 | 84 Mandatory | `LC_Shrub` | Mandatory | 1.0–10.0 | height 2.0–5.0 | LC_VegetationArtificialityCharacteristic |
| 80 | 87 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 40.0–100.0 | height 80.0–200.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `7F`.
