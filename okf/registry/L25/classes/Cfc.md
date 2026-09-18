---
id: registry:L25:Cfc
kind: class
title: Cfc Forest plantation deciduous
system: registry:L25
code: Cfc
name: Forest plantation deciduous
status: registered
decomposed: true
file_class_id: 1A4
n_rows: 27
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Cfc Forest plantation deciduous

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of the deciduous forest plantation. It is composed of a single mandatory stratum that defines the overall structure of the class.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1A5 | 1A6 Mandatory | `LC_Tree` | Mandatory |  | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Deciduous]/name=Deciduous; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Deciduous]/description=Describe a Deciduous leaf phenology element | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed, elements/LC_Characteristic[LC_Plantation]/name=Plantation) |

Full rows: `../elements.csv`, class_id `1A4`.
