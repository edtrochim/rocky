---
id: registry:L32:Mf
kind: class
title: Mf Mixed forest
system: registry:L32
code: Mf
name: Mixed forest
status: registered
decomposed: true
file_class_id: '15'
n_rows: 27
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L32
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L32/L32.lccs
schema: okf/0.1
---

# Mf Mixed forest

## Definition (verbatim, FAO LCLR)

Mixed forest land includes all forested areas where both evergreen and deciduous trees are growing and neither predominates.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 16 | 17 Mandatory | `LC_Tree` | Mandatory |  | LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/name=Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/description=Contains the elements of Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Broadleaved]/name=Broadleaved; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Broadleaved]/description=Describe a Broadleaved type element; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Needleleaved]/name=Needleleaved; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Needleleaved]/description=Describe a Needleleaved type element | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `15`.
