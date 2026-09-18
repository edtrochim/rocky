---
id: registry:L35:TF
kind: class
title: TF Closed to open trees on temporarily flooded land
system: registry:L35
code: TF
name: Closed to open trees on temporarily flooded land
status: registered
decomposed: true
file_class_id: BA
n_rows: 33
rows_in: ../elements.csv
element_refs:
- LC_Tree
- LC_WaterBody
links:
- rel: in_system
  id: registry:L35
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L35/L35.lccs
schema: okf/0.1
---

# TF Closed to open trees on temporarily flooded land

## Definition (verbatim, FAO LCLR)

NA

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| BB | 161 Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Hours; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/period_type=Temporary |  |
| BB | BC Mandatory | `LC_Tree` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `BA`.
