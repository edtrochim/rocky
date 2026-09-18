---
id: registry:L25:Cpf
kind: class
title: Cpf Forest plantation
system: registry:L25
code: Cpf
name: Forest plantation
status: registered
decomposed: true
file_class_id: 18C
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

# Cpf Forest plantation

## Definition (verbatim, FAO LCLR)

This class is very basic, and generic being constituted by one mandatory stratum that defines the overall class structure. The strata are constituted by one basic element tree and it is rainfed forest plantation area.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 18D | 18E Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_Plantation]/name=Plantation) |

Full rows: `../elements.csv`, class_id `18C`.
