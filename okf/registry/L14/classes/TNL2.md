---
id: registry:L14:TNL2
kind: class
title: TNL2 Open needle-leaved trees
system: registry:L14
code: TNL2
name: Open needle-leaved trees
status: registered
decomposed: true
file_class_id: 6F
n_rows: 33
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L14
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L14/L14.lccs
schema: okf/0.1
---

# TNL2 Open needle-leaved trees

## Definition (verbatim, FAO LCLR)

Closed needle-leaved trees (10%-40%)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 70 | 71 Mandatory | `LC_Tree` | Mandatory | 5.0–40.0 | LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/name=Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/description=Contains the elements of Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Needleleaved]/name=Needleleaved; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Needleleaved]/description=Describe a Needleleaved type element | LC_VegetationArtificialityCharacteristic |
| 70 | FC Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `6F`.
