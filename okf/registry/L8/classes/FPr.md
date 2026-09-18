---
id: registry:L8:FPr
kind: class
title: FPr Rubber plantation
system: registry:L8
code: FPr
name: Rubber plantation
status: registered
decomposed: true
file_class_id: 1AE
n_rows: 38
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

# FPr Rubber plantation

## Definition (verbatim, FAO LCLR)

The large area where rubber (Hevea brasiliensis) is planted for latex production. Trees are planted in well-drained soil with 3%-32% slope. It is broadleaved, deciduous in the drier month for a very short period. It grows 30 – 40 m and cover ranging from 80% – 100%.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1AF | 1B0 Mandatory | `LC_Tree` | Mandatory | 10.0–100.0 | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Deciduous]/name=Deciduous; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Deciduous]/description=Describe a Deciduous leaf phenology element; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/name=Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/description=Contains the elements of Woody Growth Leaf Type | LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Rubber); LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Plantation]/name=Plantation, elements/LC_Characteristic[LC_Plantation]/description=Describe the plantation, elements/LC_Characteristic[LC_PlantSpreadingGeometry]/name=Plant Spreading Geometry) |

Full rows: `../elements.csv`, class_id `1AE`.
