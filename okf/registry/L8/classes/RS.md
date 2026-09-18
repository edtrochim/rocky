---
id: registry:L8:RS
kind: class
title: RS Rural settlement
system: registry:L8
code: RS
name: Rural settlement
status: registered
decomposed: true
file_class_id: 13A
n_rows: 61
rows_in: ../elements.csv
element_refs:
- LC_Building
- LC_HerbaceousGrowthForm
- LC_Tree
- LC_WaterBody
links:
- rel: in_system
  id: registry:L8
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Building
  path: ../../../vocab/elements/LC_Building.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L8/L8.lccs
schema: okf/0.1
---

# RS Rural settlement

## Definition (verbatim, FAO LCLR)

Geographic areas of clustered or linear rural dwelling (mainly wooden and tin roof) covered by fruit trees and other plantation and functionally linked with small scale vegetables gardens, open spaces and ponds around the dwellings. Rural markets or growth centers within the rural environment are also included in this class.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 13B | 13C Mandatory | `LC_Tree` | Mandatory | 40.0–60.0 | height 5.0–30.0 | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation); LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Fruit Trees and Wood Timber) |
| 13B | 13C Mandatory | `LC_HerbaceousGrowthForm` | Optional |  |  | LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Vegetables and Fruits); LC_CultivatedAndManagedVegetationCharacteristics |
| 13B | 13C Mandatory | `LC_Building` | Mandatory | 20.0–30.0 | construction_material=Mainly light material |  |
| 13B | 13C Mandatory | `LC_WaterBody` | Mandatory | 10.0–20.0 | dynamics=Standing; position=Above Surface | LC_ArtificialityCharacteristic (type=Artificial); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `13A`.
