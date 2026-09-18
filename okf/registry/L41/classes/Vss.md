---
id: registry:L41:Vss
kind: class
title: Vss Very Open/Sparse Shrub Dominated
system: registry:L41
code: Vss
name: Very Open/Sparse Shrub Dominated
status: registered
decomposed: true
file_class_id: '34'
n_rows: 66
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L41
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L41/L41.lccs
schema: okf/0.1
---

# Vss Very Open/Sparse Shrub Dominated

## Definition (verbatim, FAO LCLR)

Sparse shrub cover (4-20%), found in degraded shrublands or steppe-forest transition zones.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 35 | 36 Mandatory | `LC_Shrub` | Mandatory | 4.0–20.0 | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Deciduous]/name=Deciduous; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Deciduous]/description=Describe a Deciduous leaf phenology element; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/name=Evergreen; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/description=Describe an Evergreen leaf phenology element | LC_VegetationArtificialityCharacteristic |
| 35 | 137 Optional | `LC_Tree` | Mandatory |  | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Deciduous]/name=Deciduous; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Deciduous]/description=Describe a Deciduous leaf phenology element; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/name=Evergreen; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/description=Describe an Evergreen leaf phenology element | LC_VegetationArtificialityCharacteristic |
| 35 | 13F Optional | `LC_HerbaceousGrowthForm` | Mandatory |  | LC_HerbaceousGrowthLeafPhenology[LC_HerbaceousGrowthLeafPhenology]/name=Herbaceous Growth Leaf Phenology; LC_HerbaceousGrowthLeafPhenology[LC_HerbaceousGrowthLeafPhenology]/description=Contains the elements of Herbaceous Growth Leaf Phenology; LC_HerbaceousGrowthLeafPhenology[LC_HerbaceousGrowthLeafPhenology]/elements/LC_HerbaceousLeafPhenology[LC_Perennial]/name=Perennial; LC_HerbaceousGrowthLeafPhenology[LC_HerbaceousGrowthLeafPhenology]/elements/LC_HerbaceousLeafPhenology[LC_Perennial]/description=Describe a Perennial herbaceous growth form leaf phenology | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `34`.
