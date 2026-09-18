---
id: registry:L48:IC
kind: class
title: IC Irrigated crops
system: registry:L48
code: IC
name: Irrigated crops
status: registered
decomposed: true
file_class_id: '3'
n_rows: 19
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L48
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L48/L48.lccs
schema: okf/0.1
---

# IC Irrigated crops

## Definition (verbatim, FAO LCLR)

Cropland where the water source comes from irrigation. Most of the crops planted are vegetables. The most common cultivated crops in this category include herbaceous crops such as strawberry, sweet pepper, tomato, cauliflower, carrot, cucumber, celery, eggplant, pumpkin, fennel, okra, squash, lettuce, watermelon, garlic, onion, maize, sunflower, potato, chickpea, lentil, green bean, pea, coriander, dill, mint, oregano, parsley. Cultivated usually in summer, the distance between rows is around 1.5 m, but for potato, cauliflower, cabbage, carrot, celery, lettuce, garlic, onion, it is 0.75 to 1 m. No space is required for mint, dill, and parsley.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4 | 5 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Irrigation]/name=Irrigation, elements/LC_Characteristic[LC_Irrigation]/description=Describe the irrigation) |

Full rows: `../elements.csv`, class_id `3`.
