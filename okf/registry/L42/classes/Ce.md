---
id: registry:L42:Ce
kind: class
title: Ce Cereals
system: registry:L42
code: Ce
name: Cereals
status: registered
decomposed: true
file_class_id: '52'
n_rows: 33
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_Graminoid
links:
- rel: in_system
  id: registry:L42
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_Graminoid
  path: ../../../vocab/elements/LC_Graminoid.md
sources:
- okf/registry/_raw/L42/L42.lccs
schema: okf/0.1
---

# Ce Cereals

## Definition (verbatim, FAO LCLR)

A cereal refers to any grass plant grown for its edible grains (seeds), which are a staple food source. Cereals grow in Akkar, North Lebanon, and other areas. The term also applies to the grains themselves, which are rich in carbohydrates. Usually, cereals in Lebanon consists of wheat, barley, and corn.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 53 | 54 Mandatory | `LC_Graminoid` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation); LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Cereals) |
| 53 | 5A Mandatory | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `52`.
