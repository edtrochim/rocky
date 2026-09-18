---
id: registry:L11:Hco
kind: class
title: Hco Herbaceous crops and orchards
system: registry:L11
code: Hco
name: Herbaceous crops and orchards
status: registered
decomposed: true
file_class_id: 1E
n_rows: 27
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L11
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L11/L11.lccs
schema: okf/0.1
---

# Hco Herbaceous crops and orchards

## Definition (verbatim, FAO LCLR)

Herbaceous crops + irregular/regular orchards plantations.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1F | 20 Mandatory | `LC_Tree` | Mandatory | 10.0–100.0 |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation) |
| 1F | 20 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `1E`.
