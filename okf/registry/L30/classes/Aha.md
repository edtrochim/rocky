---
id: registry:L30:Aha
kind: class
title: Aha Improved grasslands
system: registry:L30
code: Aha
name: Improved grasslands
status: registered
decomposed: true
file_class_id: 6D
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L30
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L30/L30.lccs
schema: okf/0.1
---

# Aha Improved grasslands

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 6E | 6F Mandatory | `LC_HerbaceousGrowthForm` | Exclusive |  | LC_HerbaceousGrowthLeafPhenology[LC_HerbaceousGrowthLeafPhenology]/name=Herbaceous Growth Leaf Phenology; LC_HerbaceousGrowthLeafPhenology[LC_HerbaceousGrowthLeafPhenology]/description=Contains the elements of Herbaceous Growth Leaf Phenology; LC_HerbaceousGrowthLeafPhenology[LC_HerbaceousGrowthLeafPhenology]/elements/LC_HerbaceousLeafPhenology[LC_Annual]/name=Annual; LC_HerbaceousGrowthLeafPhenology[LC_HerbaceousGrowthLeafPhenology]/elements/LC_HerbaceousLeafPhenology[LC_Annual]/description=Describe an Annual herbaceous growth form leaf phenology | LC_CultivatedAndManagedVegetationCharacteristics |
| 6E | 6F Mandatory | `LC_Shrub` | Exclusive |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Plantation]/name=Plantation, elements/LC_Characteristic[LC_Plantation]/description=Describe the plantation) |

Full rows: `../elements.csv`, class_id `6D`.
