---
id: registry:L42:Df
kind: class
title: Df Deciduous forest
system: registry:L42
code: Df
name: Deciduous forest
status: registered
decomposed: true
file_class_id: A
n_rows: 36
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L42
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L42/L42.lccs
schema: okf/0.1
---

# Df Deciduous forest

## Definition (verbatim, FAO LCLR)

Dense deciduous forests include areas with plant cover composed of more than 70% deciduous trees, with bushes and shrubs in the undergrowth

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| B | 11 Mandatory | `LC_Shrub` | Mandatory | 10.0–50.0 | height 4.0–5.0 | LC_VegetationArtificialityCharacteristic |
| B | C Mandatory | `LC_Tree` | Mandatory | 80.0–100.0 | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Deciduous]/name=Deciduous; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Deciduous]/description=Describe a Deciduous leaf phenology element; height 5.0–30.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `A`.
