---
id: registry:L21:B
kind: class
title: B Bamboo
system: registry:L21
code: B
name: Bamboo
status: registered
decomposed: true
file_class_id: '85'
n_rows: 34
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L21
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L21/L21.lccs
schema: okf/0.1
---

# B Bamboo

## Definition (verbatim, FAO LCLR)

Area dominated by bamboo.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 86 | 87 Mandatory | `LC_Tree` | Mandatory | 65.0–100.0 | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/name=Evergreen; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/description=Describe an Evergreen leaf phenology element; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/percentage 100.0–100.0; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/name=Woody Growth Leaf Type | LC_VegetationArtificialityCharacteristic; LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_SinglePlantSpecies]/name=Single Plant Species, elements/LC_Characteristic[LC_SinglePlantSpecies]/description=Describe a floristic aspect of single plant species, elements/LC_Characteristic[LC_SinglePlantSpecies]/type=Dominant) |

Full rows: `../elements.csv`, class_id `85`.
