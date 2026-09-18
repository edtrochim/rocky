---
id: registry:L21:Fr
kind: class
title: Fr Forest regrowth
system: registry:L21
code: Fr
name: Forest regrowth
status: registered
decomposed: true
file_class_id: '26'
n_rows: 70
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L21
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
- okf/registry/_raw/L21/L21.lccs
schema: okf/0.1
---

# Fr Forest regrowth

## Definition (verbatim, FAO LCLR)

Areas of naturally regenerated forest where there are clearly visible indication of human activities such as selective logging, areas regenerating following agricultural land use, areas recovering from human induced fire, etc. It include forest where it is not possible to distinguish whether planted or naturally regeneration; include forests with mix of naturally regenerated trees and planted/seeded trees, and where the naturally regenerated trees are expected to constitute more than 50 percent of the growing stock at stand maturity; Include abandoned forest land and bare land which will regrow into forest within ten years.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 27 | 28 Optional | `LC_HerbaceousGrowthForm` | Mandatory | 0.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 27 | 2B Optional | `LC_Shrub` | Mandatory | 0.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 27 | 2E Mandatory | `LC_Tree` | Mandatory | 10.0–100.0 | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/name=Evergreen; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/description=Describe an Evergreen leaf phenology element; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/percentage 100.0–100.0; LC_WoodyGrowthLeafType[LC_WoodyGrowthLeafType]/name=Woody Growth Leaf Type | LC_VegetationArtificialityCharacteristic; LC_UserDefinedElementCharacteristic (userid=uds_813a8610-1864-11e4-852a-18037338e6a5) |
| 81 | 82 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_UserDefinedElementCharacteristic (userid=uds_80355321-5669-11e3-8284-782bcba463ca) |

Full rows: `../elements.csv`, class_id `26`.
