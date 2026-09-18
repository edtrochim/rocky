---
id: registry:L8:FWa
kind: class
title: FWa Fresh water aquaculture
system: registry:L8
code: FWa
name: Fresh water aquaculture
status: registered
decomposed: true
file_class_id: 36E
n_rows: 38
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L8
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L8/L8.lccs
schema: okf/0.1
---

# FWa Fresh water aquaculture

## Definition (verbatim, FAO LCLR)

Fresh water ponds used for year round aquaculture.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 36F | 370 Mandatory | `LC_HerbaceousGrowthForm` | Optional |  |  | LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Rice) |
| 36F | 370 Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Standing; position=Above Surface | LC_ArtificialityCharacteristic (type=Artificial); LC_AquacultureCharacteristic (type=Fresh Water Fish); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `36E`.
