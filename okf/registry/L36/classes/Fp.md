---
id: registry:L36:Fp
kind: class
title: Fp Rainfed orchards
system: registry:L36
code: Fp
name: Rainfed orchards
status: registered
decomposed: true
file_class_id: C3
n_rows: 29
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_Tree
links:
- rel: in_system
  id: registry:L36
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L36/L36.lccs
schema: okf/0.1
---

# Fp Rainfed orchards

## Definition (verbatim, FAO LCLR)

The land is covered by rainfed orchards cultivated for the production of fruits (i.e., orange, citrus, fig, apple, peach and apricot), and other type of plantations

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| C4 | 20F Optional | `LC_BareSoil` | Mandatory |  |  |  |
| C4 | C5 Mandatory | `LC_Tree` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation, elements/LC_Characteristic[LC_Rainfed]/name=Rainfed) |

Full rows: `../elements.csv`, class_id `C3`.
