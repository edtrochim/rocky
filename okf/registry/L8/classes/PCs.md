---
id: registry:L8:PCs
kind: class
title: PCs Single crop
system: registry:L8
code: PCs
name: Single crop
status: registered
decomposed: true
file_class_id: 17B
n_rows: 33
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L8
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L8/L8.lccs
schema: okf/0.1
---

# PCs Single crop

## Definition (verbatim, FAO LCLR)

This class includes permanent agriculture lands cultivated with a single herbaceous crop in a year and the same herbaceous crop is cultivated in the same land for several years. Fields may be flooded in monsoon but not in the growing season.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 17C | 17D Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  | LC_HerbaceousGrowthLeafPhenology[LC_HerbaceousGrowthLeafPhenology]/name=Herbaceous Growth Leaf Phenology; LC_HerbaceousGrowthLeafPhenology[LC_HerbaceousGrowthLeafPhenology]/description=Contains the elements of Herbaceous Growth Leaf Phenology; LC_HerbaceousGrowthLeafPhenology[LC_HerbaceousGrowthLeafPhenology]/elements/LC_HerbaceousLeafPhenology[LC_Annual]/name=Annual; LC_HerbaceousGrowthLeafPhenology[LC_HerbaceousGrowthLeafPhenology]/elements/LC_HerbaceousLeafPhenology[LC_Annual]/description=Describe an Annual herbaceous growth form leaf phenology | LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Cereals and Fruits); LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_PlantSpreadingGeometry]/name=Plant Spreading Geometry, elements/LC_Characteristic[LC_PlantSpreadingGeometry]/description=Describe the plant spreading geometry, elements/LC_Characteristic[LC_PlantSpreadingGeometry]/type=Regular) |

Full rows: `../elements.csv`, class_id `17B`.
