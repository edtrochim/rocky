---
id: registry:L35:SRC
kind: class
title: SRC Small rice crops
system: registry:L35
code: SRC
name: Small rice crops
status: registered
decomposed: true
file_class_id: '80'
n_rows: 28
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

# SRC Small rice crops

## Definition (verbatim, FAO LCLR)

NA

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 81 | 82 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_SinglePlantSpecies]/name=Single Plant Species, elements/LC_Characteristic[LC_SinglePlantSpecies]/description=Describe a floristic aspect of single plant species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species); LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_FieldSize]/name=Field Size, elements/LC_Characteristic[LC_FieldSize]/description=Describe the field size) |

Full rows: `../elements.csv`, class_id `80`.
