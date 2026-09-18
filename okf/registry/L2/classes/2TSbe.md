---
id: registry:L2:2TSbe
kind: class
title: 2TSbe Sparse broadleaved trees
system: registry:L2
code: 2TSbe
name: Sparse broadleaved trees
status: registered
decomposed: true
file_class_id: B2
n_rows: 27
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L2
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L2/L2.lccs
schema: okf/0.1
---

# 2TSbe Sparse broadleaved trees

## Definition (verbatim, FAO LCLR)

Trees sparse (1-15%), broadleaved evergreen

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| B3 | B4 Mandatory | `LC_Tree` | Mandatory | 1.0–15.0 | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/name=Evergreen; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/description=Describe an Evergreen leaf phenology element; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/name=Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/description=Contains the elements of Woody Growth Leaf Type | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `B2`.
