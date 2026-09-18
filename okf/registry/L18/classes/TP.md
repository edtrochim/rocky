---
id: registry:L18:TP
kind: class
title: TP Tea plantations
system: registry:L18
code: TP
name: Tea plantations
status: registered
decomposed: true
file_class_id: 3E
n_rows: 23
rows_in: ../elements.csv
element_refs:
- LC_Shrub
links:
- rel: in_system
  id: registry:L18
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L18/L18.lccs
schema: okf/0.1
---

# TP Tea plantations

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3F | 40 Mandatory | `LC_Shrub` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics; LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Tea) |

Full rows: `../elements.csv`, class_id `3E`.
