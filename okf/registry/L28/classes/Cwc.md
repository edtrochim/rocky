---
id: registry:L28:Cwc
kind: class
title: Cwc Cultivated land wooded crops
system: registry:L28
code: Cwc
name: Cultivated land wooded crops
status: registered
decomposed: true
file_class_id: '78'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L28
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L28/L28.lccs
schema: okf/0.1
---

# Cwc Cultivated land wooded crops

## Definition (verbatim, FAO LCLR)

Monocultures and mixed crops of Tea, Cashew nuts, Cloves, mangoes, oranges etc.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 79 | 7A Mandatory | `LC_WoodyGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation) |

Full rows: `../elements.csv`, class_id `78`.
