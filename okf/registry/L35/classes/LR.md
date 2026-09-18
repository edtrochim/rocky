---
id: registry:L35:LR
kind: class
title: LR Large to medium rice crops (rotational)
system: registry:L35
code: LR
name: Large to medium rice crops (rotational)
status: registered
decomposed: true
file_class_id: '78'
n_rows: 43
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L35
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L35/L35.lccs
schema: okf/0.1
---

# LR Large to medium rice crops (rotational)

## Definition (verbatim, FAO LCLR)

NA

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 79 | 156 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics; LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Mais and other crops) |
| 79 | 7A Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics; LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_SinglePlantSpecies]/name=Single Plant Species, elements/LC_Characteristic[LC_SinglePlantSpecies]/description=Describe a floristic aspect of single plant species, elements/LC_Characteristic[LC_SinglePlantSpecies]/type=Most Frequent) |

Full rows: `../elements.csv`, class_id `78`.
