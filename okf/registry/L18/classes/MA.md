---
id: registry:L18:MA
kind: class
title: MA Maize
system: registry:L18
code: MA
name: Maize
status: registered
decomposed: true
file_class_id: 1D
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

# MA Maize

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1E | 1F Mandatory | `LC_Graminoid` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics; LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Maize) |

Full rows: `../elements.csv`, class_id `1D`.
