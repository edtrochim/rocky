---
id: registry:L14:HCT
kind: class
title: HCT Herbaceous crop rainfed + orchard plantation
system: registry:L14
code: HCT
name: Herbaceous crop rainfed + orchard plantation
status: registered
decomposed: true
file_class_id: '32'
n_rows: 40
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L14
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L14/L14.lccs
schema: okf/0.1
---

# HCT Herbaceous crop rainfed + orchard plantation

## Definition (verbatim, FAO LCLR)

Rainfed cultivation of herbaceous crops + rainfed orchard plantation (olive)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 33 | 34 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed) |
| 126 | 127 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed); LC_FloristicAspectsCharacteristic (elements/LC_Characteristic[LC_FloristicAspectSpecies]/name=Floristic Aspect Species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/description=Describe the floristic aspect species, elements/LC_Characteristic[LC_FloristicAspectSpecies]/species_name=Olive) |

Full rows: `../elements.csv`, class_id `32`.
