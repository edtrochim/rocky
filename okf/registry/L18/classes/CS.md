---
id: registry:L18:CS
kind: class
title: CS Cassava
system: registry:L18
code: CS
name: Cassava
status: registered
decomposed: true
file_class_id: '24'
n_rows: 34
rows_in: ../elements.csv
element_refs:
- LC_Graminoid
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L18
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Graminoid
  path: ../../../vocab/elements/LC_Graminoid.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L18/L18.lccs
schema: okf/0.1
---

# CS Cassava

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 25 | 26 Mandatory | `LC_Graminoid` | Mandatory |  |  | LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Cassava); LC_CultivatedAndManagedVegetationCharacteristics |
| 25 | 73 Optional | `LC_WoodyGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `24`.
