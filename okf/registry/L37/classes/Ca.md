---
id: registry:L37:Ca
kind: class
title: Ca Annual cultivation
system: registry:L37
code: Ca
name: Annual cultivation
status: registered
decomposed: true
file_class_id: '82'
n_rows: 24
rows_in: ../elements.csv
element_refs:
- LC_GrowthForm
links:
- rel: in_system
  id: registry:L37
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_GrowthForm
  path: ../../../vocab/elements/LC_GrowthForm.md
sources:
- okf/registry/_raw/L37/L37.LChS
schema: okf/0.1
---

# Ca Annual cultivation

## Definition (verbatim, FAO LCLR)

These are crops grown regularly each year and dependent on the rainfall regime. They are made up of cereal crops (millet, corn, sorghum, cotton, etc.), fodder crops, those produced for food seasoning and medical needs, as well as oilseeds and certain vegetable crops such as okra. The plant cover in these units is less than 25% and they are recognizable in the images by the structure of the plot and the plant cover combined with the nature of the soil, in particular the types of materials in place. There are also irrigated crops: these types of crops are grown using appropriate arrangements allowing the supply of water by gravity, by sprinkling or by dripping. This is linked to the fact that these crops are grown in the dry season, which is why their identification on the image is done using scenes taken on the dates of production of these crops. These crops are easily identifiable in the images by their geometric shapes, the presence of developments and the contrast they cause in the dry season. They are practiced alternating with rainfed crops. The main products are: tomatoes, onions, cabbages, green beans, potatoes, rice etc.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 83 | 84 Mandatory | `LC_GrowthForm` | Mandatory | 0–25 |  | LC_CultivatedAndManagedVegetationCharacteristics; LC_CultivatedAndManagedVegetationCharacteristics; LC_FloristicAspectsCharacteristic (speciesName=Millet); LC_FloristicAspectsCharacteristic |

Full rows: `../elements.csv`, class_id `82`.
