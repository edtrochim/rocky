---
id: registry:L8:PCm
kind: class
title: PCm Multiple crop
system: registry:L8
code: PCm
name: Multiple crop
status: registered
decomposed: true
file_class_id: 3B0
n_rows: 61
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L8
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L8/L8.lccs
schema: okf/0.1
---

# PCm Multiple crop

## Definition (verbatim, FAO LCLR)

This class includes permanent agriculture lands which are cultivated with more than one herbaceous crop (Two or Three) in different growing season sequentially (crop diversified in time) within a year and the same crop rotation is practiced in the same land for several years.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3B1 | 3B2 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed); LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Rice) |
| 3B1 | 3B2 Mandatory | `LC_HerbaceousGrowthForm` | Optional |  |  | LC_VegetationArtificialityCharacteristic |
| 3B1 | 3B2 Mandatory | `LC_HerbaceousGrowthForm` | Optional |  |  | LC_CultivatedAndManagedVegetationCharacteristics; LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Pulses and Vegetables) |
| 3B1 | 3B2 Mandatory | `LC_HerbaceousGrowthForm` | Optional |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation, elements/LC_Characteristic[LC_Irrigation]/irrigation_type=Surface/ground water); LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Rice) |

Full rows: `../elements.csv`, class_id `3B0`.
