---
id: registry:L34
kind: system
title: Sub-national land cover legend for Mozambique
alpha_code: L34
country: Mozambique
m49: 508
iso3: MOZ
year: 2022
status: valid
legend_type: LCCS3
format: lccs3
publisher: Food and Agriculture Organization of the United Nations
reference_link: Coming soon
reference_file: ''
n_classes_index: 12
n_classes_file: 12
n_classes_matched: 12
n_datasets: 1
files:
- okf/registry/_raw/L34/L34.csv
- okf/registry/_raw/L34/L34.eapx
- okf/registry/_raw/L34/L34.lccs
- okf/registry/_raw/L34/L34.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L34:In
  path: classes/In.md
- rel: has_class
  id: registry:L34:Fo
  path: classes/Fo.md
- rel: has_class
  id: registry:L34:Cl
  path: classes/Cl.md
- rel: has_class
  id: registry:L34:Bs
  path: classes/Bs.md
- rel: has_class
  id: registry:L34:Sv
  path: classes/Sv.md
- rel: has_class
  id: registry:L34:Me
  path: classes/Me.md
- rel: has_class
  id: registry:L34:Sc
  path: classes/Sc.md
- rel: has_class
  id: registry:L34:Ma
  path: classes/Ma.md
- rel: has_class
  id: registry:L34:Wa
  path: classes/Wa.md
- rel: has_class
  id: registry:L34:We
  path: classes/We.md
- rel: has_class
  id: registry:L34:Gr
  path: classes/Gr.md
- rel: has_class
  id: registry:L34:Or
  path: classes/Or.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# Sub-national land cover legend for Mozambique

Mozambique · 2022 · LCCS3 · status valid. Publisher: Food and Agriculture Organization of the United Nations. 12 classes in the registry index, 12 in the legend file, 12 matched by code or name.

Reference: Mapping land cover in the Maputo and Gaza provinces in Mozambique (2024), Coming soon

## Datasets (1)

- Mapping land cover in the Maputo and Gaza provinces in Mozambique (iso/c08a26c9-2aea-4003-a848-5a7d419e277a)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| In | [Infrastructure](classes/In.md) | This land is characterized by the presence of buildings, roads and artificial surfaces. Different types of bu… |
| Fo | [Forest](classes/Fo.md) | This land is characterized by the presence of dense natural forests, bushes and shrubs are also common in the… |
| Cl | [Cultivated land](classes/Cl.md) | This land consists of agricultural fields which may feature various types of crops such as wheat and barley, … |
| Bs | [Bare soil](classes/Bs.md) | This land consists of bare soil which is not used for cultivation and usually devoid of grass and shrub cover. |
| Sv | [Spare vegetation](classes/Sv.md) | This land is categorized by bare soil which is sparsely populated with shrubs and grasses. This land is unman… |
| Me | [Meadow](classes/Me.md) | This land consists of relatively dense herbaceous natural vegetation, occasionally populated by sparse shrubs… |
| Sc | [Sugarcane](classes/Sc.md) | This class consists of agricultural land which is used for the cultivation of sugarcane. |
| Ma | [Mangrove](classes/Ma.md) | This class consists of intertidal forest land. It is characterized by the presence of trees and water bodies. |
| Wa | [Water](classes/Wa.md) | This land is characterized by the presence of water bodies, including both natural and artificial non - peren… |
| We | [Wetland](classes/We.md) | This class consists of swamp and wetland areas in which herbaceous or aquaic vegetation are present. It may i… |
| Gr | [Grassland](classes/Gr.md) | This class is categorized by the prevalence of herbaceous vegetation, mainly grasses, with sparse trees or sh… |
| Or | [Orchard](classes/Or.md) | This land consists of orchards cultivated for the production of fruits (i.e. organge, citrus, fig, apple, pea… |
