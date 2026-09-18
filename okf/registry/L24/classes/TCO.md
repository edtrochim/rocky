---
id: registry:L24:TCO
kind: class
title: TCO Forest
system: registry:L24
code: TCO
name: Forest
status: registered
decomposed: true
file_class_id: '24'
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L24
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L24/L24.lccs
schema: okf/0.1
---

# TCO Forest

## Definition (verbatim, FAO LCLR)

Trees closed-to-sparse in terrestrial and aquatic/regularly flooded land.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 25 | 26 Mandatory | `LC_Tree` | Mandatory |  | LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/name=Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/description=Contains the elements of Woody Growth Leaf Type; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Broadleaved]/name=Broadleaved; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/elements/LC_WoodyLeafType[LC_Broadleaved]/description=Describe a Broadleaved type element; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology | LC_VegetationArtificialityCharacteristic; LC_UserDefinedElementCharacteristic (userid=uds_cf536350-ea75-11e5-a049-780cb82883be, LC_Property[LC_PropertyDouble@minimum_area_size_ha]/value=0.4) |

Full rows: `../elements.csv`, class_id `24`.
