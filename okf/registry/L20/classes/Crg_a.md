---
id: registry:L20:Crg_a
kind: class
title: Crg_a Rice field
system: registry:L20
code: Crg_a
name: Rice field
status: registered
decomposed: true
file_class_id: '83'
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_Graminoid
links:
- rel: in_system
  id: registry:L20
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Graminoid
  path: ../../../vocab/elements/LC_Graminoid.md
sources:
- okf/registry/_raw/L20/L20.lccs
schema: okf/0.1
---

# Crg_a Rice field

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 84 | 85 Mandatory | `LC_Graminoid` | Mandatory | 40.0–60.0 |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_FieldSize]/name=Field Size, elements/LC_Characteristic[LC_FieldSize]/description=Describe the field size, elements/LC_Characteristic[LC_Irrigation]/name=Irrigation); LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Rice) |

Full rows: `../elements.csv`, class_id `83`.
