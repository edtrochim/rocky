---
id: registry:L18:PR
kind: class
title: PR Paddy rice
system: registry:L18
code: PR
name: Paddy rice
status: registered
decomposed: true
file_class_id: '2'
n_rows: 28
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

# PR Paddy rice

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4 | 5 Mandatory | `LC_Graminoid` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation, elements/LC_Characteristic[LC_Irrigation]/irrigation_type=Surface); LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Rice) |

Full rows: `../elements.csv`, class_id `2`.
