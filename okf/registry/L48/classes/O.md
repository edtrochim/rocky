---
id: registry:L48:O
kind: class
title: O Orchards or home garden
system: registry:L48
code: O
name: Orchards or home garden
status: registered
decomposed: true
file_class_id: F
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L48
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L48/L48.lccs
schema: okf/0.1
---

# O Orchards or home garden

## Definition (verbatim, FAO LCLR)

Cropland that are covered by shrubs or trees crops which can be either mixed or single type. The crops cover the land permanently. Shrubs/Herbs crops can be optional on the second layer/strata. The most common crops include olives, citrus, date palm, almonds, lemon, and grapes. Each crop has distinct distance between rows.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 10 | 11 Mandatory | `LC_WoodyGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/name=Orchard And Other Plantation, elements/LC_Characteristic[LC_OrchardAndOtherPlantation]/description=Describe the orchard and other plantation) |
| 10 | 15 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `F`.
