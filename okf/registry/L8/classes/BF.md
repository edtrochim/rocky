---
id: registry:L8:BF
kind: class
title: BF Bamboo forest
system: registry:L8
code: BF
name: Bamboo forest
status: registered
decomposed: true
file_class_id: '205'
n_rows: 36
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L8
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L8/L8.lccs
schema: okf/0.1
---

# BF Bamboo forest

## Definition (verbatim, FAO LCLR)

Bamboo forest is woody grass of more than 4 m and its occurrence is more than 80% within the patches. It naturally occurs and it covers ranging from 80% - 100%. It is perennial evergreen and it grows up to 15 m. The bamboo resources in the villages areas not included in this class.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 206 | 207 Mandatory | `LC_Tree` | Mandatory | 80.0–100.0 | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/name=Evergreen; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/description=Describe an Evergreen leaf phenology element; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/name=Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/description=Contains the elements of Woody Growth Leaf Type | LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Muli, Mitenga, Dalu etc.); LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `205`.
