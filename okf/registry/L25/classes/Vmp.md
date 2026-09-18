---
id: registry:L25:Vmp
kind: class
title: Vmp Orchards (single crop) - rainfed
system: registry:L25
code: Vmp
name: Orchards (single crop) - rainfed
status: registered
decomposed: true
file_class_id: 1B7
n_rows: 23
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Vmp Orchards (single crop) - rainfed

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of the single type crop of orchards. It is composed of a single mandatory stratum that defines the overall structure of the class.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1B8 | 1B9 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_Plantation]/name=Plantation) |

Full rows: `../elements.csv`, class_id `1B7`.
