---
id: registry:L31:Shr
kind: class
title: Shr Shrubland
system: registry:L31
code: Shr
name: Shrubland
status: registered
decomposed: true
file_class_id: A7
n_rows: 37
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L31
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L31/L31.lccs
schema: okf/0.1
---

# Shr Shrubland

## Definition (verbatim, FAO LCLR)

Vegetation dominated by shrubs with 1 to 3 meters of height. Shrublands often result from losses of large areas of Miombo and Mopane forests and may include herbaceous vegetation and scattered trees.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| A8 | A9 Mandatory | `LC_Shrub` | Mandatory |  | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Deciduous]/description=Describe a Deciduous leaf phenology element; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Deciduous]/name=Deciduous; height 1.0–3.0 | LC_VegetationArtificialityCharacteristic |
| A8 | A9 Mandatory | `LC_HerbaceousGrowthForm` | Optional |  | height 1.0–200.0 | LC_VegetationArtificialityCharacteristic |
| A8 | A9 Mandatory | `LC_Tree` | Optional |  |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `A7`.
