---
id: registry:L35:RBT
kind: class
title: RBT Rainfed broadleaved evergreen tree crop(s)
system: registry:L35
code: RBT
name: Rainfed broadleaved evergreen tree crop(s)
status: registered
decomposed: true
file_class_id: '11'
n_rows: 36
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L35
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L35/L35.lccs
schema: okf/0.1
---

# RBT Rainfed broadleaved evergreen tree crop(s)

## Definition (verbatim, FAO LCLR)

NA

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 12 | 13 Mandatory | `LC_Tree` | Mandatory |  | LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/name=Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/description=Contains the elements of Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Broadleaved]/name=Broadleaved; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Broadleaved]/description=Describe a Broadleaved type element; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed); LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_SinglePlantSpecies]/name=Single Plant Species, elements/LC_Characteristic[LC_SinglePlantSpecies]/description=Describe a floristic aspect of single plant species, elements/LC_Characteristic[LC_SinglePlantSpecies]/type=Dominant) |

Full rows: `../elements.csv`, class_id `11`.
