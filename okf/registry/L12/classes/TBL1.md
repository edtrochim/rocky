---
id: registry:L12:TBL1
kind: class
title: TBL1 Trees, broadleaved (closed)
system: registry:L12
code: TBL1
name: Trees, broadleaved (closed)
status: registered
decomposed: true
file_class_id: '85'
n_rows: 26
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# TBL1 Trees, broadleaved (closed)

## Definition (verbatim, FAO LCLR)

Closed deciduous broadleaved trees, commonly along river beds, sometimws observed as plantations.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 86 | 87 Mandatory | `LC_Tree` | Mandatory | 60.0–100.0 | LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/name=Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/description=Contains the elements of Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Broadleaved]/name=Broadleaved; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Broadleaved]/description=Describe a Broadleaved type element; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `85`.
