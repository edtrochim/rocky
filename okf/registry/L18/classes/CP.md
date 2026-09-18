---
id: registry:L18:CP
kind: class
title: CP Coffee plantation
system: registry:L18
code: CP
name: Coffee plantation
status: registered
decomposed: true
file_class_id: '37'
n_rows: 31
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L18
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L18/L18.lccs
schema: okf/0.1
---

# CP Coffee plantation

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 38 | 39 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics; LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Coffee) |
| 38 | 76 Optional | `LC_Tree` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `37`.
