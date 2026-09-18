---
id: registry:L35:SRF
kind: class
title: SRF Small sized herbaceous rainfed field(s)
system: registry:L35
code: SRF
name: Small sized herbaceous rainfed field(s)
status: registered
decomposed: true
file_class_id: 6C
n_rows: 52
rows_in: ../elements.csv
element_refs:
- LC_Building
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L35
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L35/L35.lccs
schema: okf/0.1
---

# SRF Small sized herbaceous rainfed field(s)

## Definition (verbatim, FAO LCLR)

NA

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 75 | 76 Mandatory | `LC_Building` | Mandatory |  |  |  |
| 6D | 152 Mandatory | `LC_Building` | Mandatory |  |  | LC_ConstructionUse (type=rural houses) |
| 6D | 6E Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed) |
| 6D | 6E Mandatory | `LC_Shrub` | Optional |  | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_WoodyLeafPhenology]/name=Woody Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_WoodyLeafPhenology]/description=Describe a generic Woody Leaf Phenology element | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `6C`.
