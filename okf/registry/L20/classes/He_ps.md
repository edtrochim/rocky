---
id: registry:L20:He_ps
kind: class
title: He_ps Psamophilic forest
system: registry:L20
code: He_ps
name: Psamophilic forest
status: registered
decomposed: true
file_class_id: '61'
n_rows: 58
rows_in: ../elements.csv
element_refs:
- LC_Dune
- LC_Graminoid
- LC_Shrub
- LC_Tree
links:
- rel: in_system
  id: registry:L20
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Dune
  path: ../../../vocab/elements/LC_Dune.md
- rel: uses_type
  id: element:LC_Graminoid
  path: ../../../vocab/elements/LC_Graminoid.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L20/L20.lccs
schema: okf/0.1
---

# He_ps Psamophilic forest

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 62 | 63 Mandatory | `LC_Graminoid` | Mandatory | 15.0–100.0 | height 30.0–300.0 | LC_VegetationArtificialityCharacteristic |
| 62 | 66 Mandatory | `LC_Dune` | Mandatory | 100.0–100.0 |  |  |
| 62 | 11B Mandatory | `LC_Shrub` | Mandatory | 40.0–80.0 | height 0.3–3.0 | LC_VegetationArtificialityCharacteristic |
| 62 | 11D Mandatory | `LC_Tree` | Mandatory | 10.0–40.0 | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/name=Evergreen; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/description=Describe an Evergreen leaf phenology element; height 1.0–5.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `61`.
