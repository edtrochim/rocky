---
id: registry:L25:Vcp
kind: class
title: Vcp Orchards (multiple crop) - rainfed
system: registry:L25
code: Vcp
name: Orchards (multiple crop) - rainfed
status: registered
decomposed: true
file_class_id: 1BF
n_rows: 34
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

# Vcp Orchards (multiple crop) - rainfed

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of the multiple type crops of orchards. It is composed of a single mandatory stratum that defines the overall structure of the class.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1C0 | 1C1 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_Plantation]/name=Plantation) |
| 1C0 | 1C7 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `1BF`.
