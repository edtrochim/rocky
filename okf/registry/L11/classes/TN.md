---
id: registry:L11:TN
kind: class
title: TN Trees needle - leaved
system: registry:L11
code: TN
name: Trees needle - leaved
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
  id: registry:L11
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L11/L11.lccs
schema: okf/0.1
---

# TN Trees needle - leaved

## Definition (verbatim, FAO LCLR)

Evergreen needle-leaved trees (20%-100%).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 70 | 71 Mandatory | `LC_Tree` | Mandatory | 20.0–100.0 | LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/name=Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/description=Contains the elements of Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Needleleaved]/name=Needleleaved; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Needleleaved]/description=Describe a Needleleaved type element; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology | LC_VegetationArtificialityCharacteristic |
| 70 | 71 Mandatory | `LC_HerbaceousGrowthForm` | Optional |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `6F`.
