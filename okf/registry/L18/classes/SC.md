---
id: registry:L18:SC
kind: class
title: SC Sugarcane
system: registry:L18
code: SC
name: Sugarcane
status: registered
decomposed: true
file_class_id: 2B
n_rows: 23
rows_in: ../elements.csv
element_refs:
- LC_Graminoid
links:
- rel: in_system
  id: registry:L18
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Graminoid
  path: ../../../vocab/elements/LC_Graminoid.md
sources:
- okf/registry/_raw/L18/L18.lccs
schema: okf/0.1
---

# SC Sugarcane

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2C | 2D Mandatory | `LC_Graminoid` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics; LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Sugarcane) |

Full rows: `../elements.csv`, class_id `2B`.
