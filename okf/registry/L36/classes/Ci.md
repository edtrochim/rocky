---
id: registry:L36:Ci
kind: class
title: Ci Other irrigated crop
system: registry:L36
code: Ci
name: Other irrigated crop
status: registered
decomposed: true
file_class_id: 12B
n_rows: 27
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_HerbaceousGrowthForm
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
sources:
- okf/registry/_raw/L36/L36.lccs
schema: okf/0.1
---

# Ci Other irrigated crop

## Definition (verbatim, FAO LCLR)

The land is covered by irrigated agricultural fields, featuring various types of crops: cereal crops such as wheat and barley, horticultural crops like tomatoes and melonds, legumes, and forage crops. The crop water management in these areas is irrigated.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 12C | 12D Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation) |
| 12C | 22E Optional | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `12B`.
