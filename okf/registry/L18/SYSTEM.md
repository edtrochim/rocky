---
id: registry:L18
kind: system
title: National land cover legend for Lao
alpha_code: L18
country: Lao People's Democratic Republic
m49: 418
iso3: LAO
year: 2021
status: valid
legend_type: LCCS3
format: lccs3
publisher: '-'
reference_link: ''
reference_file: ''
n_classes_index: 14
n_classes_file: 14
n_classes_matched: 14
n_datasets: 1
files:
- okf/registry/_raw/L18/L18.csv
- okf/registry/_raw/L18/L18.eapx
- okf/registry/_raw/L18/L18.lccs
- okf/registry/_raw/L18/L18.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L18:AC
  path: classes/AC.md
- rel: has_class
  id: registry:L18:BA
  path: classes/BA.md
- rel: has_class
  id: registry:L18:BU
  path: classes/BU.md
- rel: has_class
  id: registry:L18:CP
  path: classes/CP.md
- rel: has_class
  id: registry:L18:CS
  path: classes/CS.md
- rel: has_class
  id: registry:L18:MA
  path: classes/MA.md
- rel: has_class
  id: registry:L18:OP
  path: classes/OP.md
- rel: has_class
  id: registry:L18:PR
  path: classes/PR.md
- rel: has_class
  id: registry:L18:SC
  path: classes/SC.md
- rel: has_class
  id: registry:L18:SSA
  path: classes/SSA.md
- rel: has_class
  id: registry:L18:TP
  path: classes/TP.md
- rel: has_class
  id: registry:L18:VGD
  path: classes/VGD.md
- rel: has_class
  id: registry:L18:VGS
  path: classes/VGS.md
- rel: has_class
  id: registry:L18:WT
  path: classes/WT.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# National land cover legend for Lao

Lao People's Democratic Republic · 2021 · LCCS3 · status valid. Publisher: -. 14 classes in the registry index, 14 in the legend file, 14 matched by code or name.

Reference: - (-), 

## Datasets (1)

- Land cover of Lao PDR (2009) (iso/5e3fec99-b303-4de9-b26c-872b033a9e07)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| AC | [Annual crops and grassland](classes/AC.md) |  |
| BA | [Bare areas](classes/BA.md) |  |
| BU | [Builtup](classes/BU.md) |  |
| CP | [Coffee plantation](classes/CP.md) |  |
| CS | [Cassava](classes/CS.md) |  |
| MA | [Maize](classes/MA.md) |  |
| OP | [Orchards and other plantations](classes/OP.md) |  |
| PR | [Paddy rice](classes/PR.md) |  |
| SC | [Sugarcane](classes/SC.md) |  |
| SSA | [Steep slope agriculture](classes/SSA.md) |  |
| TP | [Tea plantations](classes/TP.md) |  |
| VGD | [Dense natural vegetation](classes/VGD.md) |  |
| VGS | [Sparse natural vegetation](classes/VGS.md) |  |
| WT | [Water bodies](classes/WT.md) |  |
