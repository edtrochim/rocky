---
id: registry:L30:Afe
kind: class
title: Afe Hardwood plantations
system: registry:L30
code: Afe
name: Hardwood plantations
status: registered
decomposed: true
file_class_id: 1D
n_rows: 29
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L30
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L30/L30.lccs
schema: okf/0.1
---

# Afe Hardwood plantations

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1E | 1F Mandatory | `LC_Tree` | Mandatory | 0.0–0.0 | LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/name=Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/description=Contains the elements of Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Broadleaved]/name=Broadleaved; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Broadleaved]/description=Describe a Broadleaved type element; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Broadleaved]/percentage 75.0–100.0; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_ForestPlantation]/name=Forest Plantation, elements/LC_Characteristic[LC_ForestPlantation]/description=Describe the forest plantation) |

Full rows: `../elements.csv`, class_id `1D`.
