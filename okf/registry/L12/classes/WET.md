---
id: registry:L12:WET
kind: class
title: WET Wetland (perennial and/or seasonal)
system: registry:L12
code: WET
name: Wetland (perennial and/or seasonal)
status: registered
decomposed: true
file_class_id: '55'
n_rows: 52
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L12
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L12/L12.lccs
schema: okf/0.1
---

# WET Wetland (perennial and/or seasonal)

## Definition (verbatim, FAO LCLR)

Natural perennial and/or seasonal fresh waterbody + perennial closed-open natural vegetation.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 56 | 57 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 70.0–100.0 | height 30.0–100.0; LC_HerbaceousGrowthLeafPhenology[LC_HerbaceousGrowthLeafPhenology]/name=Herbaceous Growth Leaf Phenology; LC_HerbaceousGrowthLeafPhenology[LC_HerbaceousGrowthLeafPhenology]/description=Contains the elements of Herbaceous Growth Leaf Phenology; LC_HerbaceousGrowthLeafPhenology[LC_HerbaceousGrowthLeafPhenology]/elements/LC_HerbaceousLeafPhenology[LC_Perennial]/name=Perennial; LC_HerbaceousGrowthLeafPhenology[LC_HerbaceousGrowthLeafPhenology]/elements/LC_HerbaceousLeafPhenology[LC_Perennial]/description=Describe a Perennial herbaceous growth form leaf phenology | LC_VegetationArtificialityCharacteristic; LC_GrazedCharacteristic (elements/LC_Characteristic[LC_GrazingAnimalType]/name=Grazing Animal, elements/LC_Characteristic[LC_GrazingAnimalType]/description=Describe the grazing animal, elements/LC_Characteristic[LC_GrazingAnimalType]/animal_type=Domestic animals) |
| 56 | 5E Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; position=Above Surface | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `55`.
