---
id: registry:L25:Cad
kind: class
title: Cad Tree crop dominated
system: registry:L25
code: Cad
name: Tree crop dominated
status: registered
decomposed: true
file_class_id: 20A
n_rows: 21
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

# Cad Tree crop dominated

## Definition (verbatim, FAO LCLR)

It corresponds to areas with cultivated irrigated agriculture where the growth form tree is dominant.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 20B | 20C Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Plantation]/name=Plantation, elements/LC_Characteristic[LC_Plantation]/description=Describe the plantation, elements/LC_Characteristic[LC_Irrigation]/name=Irrigation) |

Full rows: `../elements.csv`, class_id `20A`.
