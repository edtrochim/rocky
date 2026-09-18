---
id: registry:L20:FP_ma
kind: class
title: FP_ma Vegetation for shelter and shade
system: registry:L20
code: FP_ma
name: Vegetation for shelter and shade
status: registered
decomposed: true
file_class_id: 1F
n_rows: 34
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L20
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L20/L20.lccs
schema: okf/0.1
---

# FP_ma Vegetation for shelter and shade

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 20 | 21 Mandatory | `LC_Tree` | Mandatory | 30.0–100.0 | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/name=Evergreen; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/description=Describe an Evergreen leaf phenology element; height 3.0–30.0 | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_ForestPlantation]/name=Forest Plantation, elements/LC_Characteristic[LC_ForestPlantation]/description=Describe the forest plantation, elements/LC_Characteristic[LC_FieldSize]/name=Field Size); LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Eucalypt) |

Full rows: `../elements.csv`, class_id `1F`.
