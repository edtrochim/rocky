---
id: registry:L36:Op
kind: class
title: Op Rainfed olives
system: registry:L36
code: Op
name: Rainfed olives
status: registered
decomposed: true
file_class_id: 13D
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

# Op Rainfed olives

## Definition (verbatim, FAO LCLR)

The land is covered by rainfed olive orchards. These cultivated groves are characterized by the sparse clustering of olive trees, forming a pattern that provides a distinctive appearance to an orchard setting with presence of bare soil.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 13E | 13F Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed); LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Olive) |
| 13E | 1FB Optional | `LC_Graminoid` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed) |
| 13E | 1FF Optional | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `13D`.
