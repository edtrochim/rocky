---
id: registry:L11:Hcr
kind: class
title: Hcr Herbaceous crop rainfed
system: registry:L11
code: Hcr
name: Herbaceous crop rainfed
status: registered
decomposed: true
file_class_id: '32'
n_rows: 27
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

# Hcr Herbaceous crop rainfed

## Definition (verbatim, FAO LCLR)

Rainfed cultivation occasionally with scattered natural trees.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 33 | 34 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed) |
| 33 | 34 Mandatory | `LC_Tree` | Optional | 1.0–20.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `32`.
