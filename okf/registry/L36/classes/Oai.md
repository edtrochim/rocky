---
id: registry:L36:Oai
kind: class
title: Oai Irrigated dates
system: registry:L36
code: Oai
name: Irrigated dates
status: registered
decomposed: true
file_class_id: '154'
n_rows: 73
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L36
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L36/L36.lccs
schema: okf/0.1
---

# Oai Irrigated dates

## Definition (verbatim, FAO LCLR)

The land is covered by irrigated date. The presence of date tress dominates the land cover (about 80 %). In some cases pomegranate trees and forage crops may be present to benefit from oasis irrigation.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 155 | 156 Mandatory | `LC_Tree` | Mandatory | 80.0–100.0 |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation, elements/LC_Characteristic[LC_Irrigation]/irrigation_type=Surface); LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Date Palm) |
| 155 | 209 Optional | `LC_Tree` | Mandatory | 1.0–30.0 |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation); LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Fruits and Nuts) |
| 155 | 226 Optional | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation) |
| 155 | 22A Optional | `LC_BareSoil` | Mandatory | 1.0–35.0 |  |  |

Full rows: `../elements.csv`, class_id `154`.
