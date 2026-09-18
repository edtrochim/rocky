---
id: registry:L30:Arm
kind: class
title: Arm Wooded shrub
system: registry:L30
code: Arm
name: Wooded shrub
status: registered
decomposed: true
file_class_id: '44'
n_rows: 43
rows_in: ../elements.csv
element_refs:
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L30
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L30/L30.lccs
schema: okf/0.1
---

# Arm Wooded shrub

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 46 | 47 Mandatory | `LC_Shrub` | Mandatory | 20.0–100.0 | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/name=Evergreen; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/description=Describe an Evergreen leaf phenology element; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/percentage 60.0–100.0; height 2.0–5.0 | LC_VegetationArtificialityCharacteristic |
| 46 | 4A Optional | `LC_Tree` | Mandatory | 2.0–9.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `44`.
