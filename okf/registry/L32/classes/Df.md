---
id: registry:L32:Df
kind: class
title: Df Deciduous or semi deciduous forest
system: registry:L32
code: Df
name: Deciduous or semi deciduous forest
status: registered
decomposed: true
file_class_id: C
n_rows: 25
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

# Df Deciduous or semi deciduous forest

## Definition (verbatim, FAO LCLR)

Deciduous for semi deciduous forest land includes all forested areas having a predominance of trees with broadleaved leaf type.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| D | E Mandatory | `LC_Tree` | Mandatory |  | LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/name=Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/description=Contains the elements of Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Broadleaved]/name=Broadleaved; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Broadleaved]/description=Describe a Broadleaved type element; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `C`.
