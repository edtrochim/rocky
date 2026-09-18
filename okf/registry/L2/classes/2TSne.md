---
id: registry:L2:2TSne
kind: class
title: 2TSne Sparse needleleaved trees
system: registry:L2
code: 2TSne
name: Sparse needleleaved trees
status: registered
decomposed: true
file_class_id: A9
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

# 2TSne Sparse needleleaved trees

## Definition (verbatim, FAO LCLR)

Sparse (1-15%) needleleaved evergreen trees

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| AA | AB Mandatory | `LC_Tree` | Mandatory | 1.0–15.0 | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/name=Evergreen; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/description=Describe an Evergreen leaf phenology element; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/name=Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/description=Contains the elements of Woody Growth Leaf Type | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `A9`.
