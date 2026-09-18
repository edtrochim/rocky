---
id: registry:L30:Ar
kind: class
title: Ar Softwood forest
system: registry:L30
code: Ar
name: Softwood forest
status: registered
decomposed: true
file_class_id: '2'
n_rows: 28
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

# Ar Softwood forest

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3 | 4 Mandatory | `LC_Tree` | Mandatory | 10.0–100.0 | LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/name=Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/description=Contains the elements of Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Needleleaved]/name=Needleleaved; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Needleleaved]/description=Describe a Needleleaved type element; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Needleleaved]/percentage 75.0–100.0; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `2`.
