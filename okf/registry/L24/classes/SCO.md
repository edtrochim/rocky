---
id: registry:L24:SCO
kind: class
title: SCO Shrubs
system: registry:L24
code: SCO
name: Shrubs
status: registered
decomposed: true
file_class_id: 2A
n_rows: 21
rows_in: ../elements.csv
element_refs:
- LC_Shrub
links:
- rel: in_system
  id: registry:L24
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L24/L24.lccs
schema: okf/0.1
---

# SCO Shrubs

## Definition (verbatim, FAO LCLR)

Shrubs closed-to-sparse in terrestrial and aquatic/regularly flooded land.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2B | 2C Mandatory | `LC_Shrub` | Mandatory |  | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Deciduous]/name=Deciduous; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Deciduous]/description=Describe a Deciduous leaf phenology element | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `2A`.
