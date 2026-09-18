---
id: registry:L36:Oi
kind: class
title: Oi Irrigated olives
system: registry:L36
code: Oi
name: Irrigated olives
status: registered
decomposed: true
file_class_id: '146'
n_rows: 46
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_Graminoid
- LC_Tree
links:
- rel: in_system
  id: registry:L36
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_Graminoid
  path: ../../../vocab/elements/LC_Graminoid.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L36/L36.lccs
schema: okf/0.1
---

# Oi Irrigated olives

## Definition (verbatim, FAO LCLR)

The land is covered by irrigated olive orchards. These cultivated groves are characterized by the sparse clustering of olive trees, forming a pattern that provides a distintive appearance to an orchard setting with presence of bare soil.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 147 | 148 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation); LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Olive) |
| 147 | 201 Optional | `LC_Graminoid` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation) |
| 147 | 205 Optional | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `146`.
