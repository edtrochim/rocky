---
id: registry:L42:Pb
kind: class
title: Pb Poultry breeding
system: registry:L42
code: Pb
name: Poultry breeding
status: registered
decomposed: true
file_class_id: '78'
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_OtherConstruction
links:
- rel: in_system
  id: registry:L42
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_OtherConstruction
  path: ../../../vocab/elements/LC_OtherConstruction.md
sources:
- okf/registry/_raw/L42/L42.lccs
schema: okf/0.1
---

# Pb Poultry breeding

## Definition (verbatim, FAO LCLR)

Poultry breeding is the place for raising domesticated birds, such as chickens, turkeys, ducks, and geese, primarily for the purpose of producing meat, eggs, or feathers

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 79 | 7A Mandatory | `LC_OtherConstruction` | Mandatory |  |  | LC_ConstructionUse (type=Breeding Center) |

Full rows: `../elements.csv`, class_id `78`.
