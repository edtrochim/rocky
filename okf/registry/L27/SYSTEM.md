---
id: registry:L27
kind: system
title: National land cover legend for Mozambique
alpha_code: L27
country: Mozambique
m49: 508
iso3: MOZ
year: 2021
status: valid
legend_type: LCCS3
format: lccs3
publisher: National Fund for Sustainable Development
reference_link: Relatorio do mapa de CF (fnds.gov.mz)
reference_file: Ref_27.pdf
n_classes_index: 18
n_classes_file: 18
n_classes_matched: 18
n_datasets: 1
files:
- okf/registry/_raw/L27/L27.eapx
- okf/registry/_raw/L27/L27.lccs
- okf/registry/_raw/L27/L27.xsd
vocabulary:
  errors: 0
  warnings: 1
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L27:1
  path: classes/1.md
- rel: has_class
  id: registry:L27:2
  path: classes/2.md
- rel: has_class
  id: registry:L27:3
  path: classes/3.md
- rel: has_class
  id: registry:L27:4
  path: classes/4.md
- rel: has_class
  id: registry:L27:5
  path: classes/5.md
- rel: has_class
  id: registry:L27:6
  path: classes/6.md
- rel: has_class
  id: registry:L27:7
  path: classes/7.md
- rel: has_class
  id: registry:L27:8
  path: classes/8.md
- rel: has_class
  id: registry:L27:9
  path: classes/9.md
- rel: has_class
  id: registry:L27:10
  path: classes/10.md
- rel: has_class
  id: registry:L27:11
  path: classes/11.md
- rel: has_class
  id: registry:L27:12
  path: classes/12.md
- rel: has_class
  id: registry:L27:13
  path: classes/13.md
- rel: has_class
  id: registry:L27:14
  path: classes/14.md
- rel: has_class
  id: registry:L27:15
  path: classes/15.md
- rel: has_class
  id: registry:L27:16
  path: classes/16.md
- rel: has_class
  id: registry:L27:17
  path: classes/17.md
- rel: has_class
  id: registry:L27:18
  path: classes/18.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# National land cover legend for Mozambique

Mozambique · 2021 · LCCS3 · status valid. Publisher: National Fund for Sustainable Development. 18 classes in the registry index, 18 in the legend file, 18 matched by code or name.

Reference: Forest coverage map of Mozambique 2016 (2019), Relatorio do mapa de CF (fnds.gov.mz)

## Datasets (1)

- Land cover map of Mozambique (-)

## Vocabulary check of the registry file

0 errors, 1 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| 1 | [Tree cultivation](classes/1.md) |  |
| 2 | [Non tree cultivation](classes/2.md) |  |
| 3 | [Forest plantation](classes/3.md) |  |
| 4 | [Prairie](classes/4.md) |  |
| 5 | [Prairie tree](classes/5.md) |  |
| 6 | [Flooded herbaceous area](classes/6.md) |  |
| 7 | [Water body](classes/7.md) |  |
| 8 | [Urban area](classes/8.md) |  |
| 9 | [Bare ground](classes/9.md) |  |
| 10 | [Rock without vegetation](classes/10.md) |  |
| 11 | [Mangrove](classes/11.md) |  |
| 12 | [Mecrusse](classes/12.md) |  |
| 13 | [Mountain forest](classes/13.md) |  |
| 14 | [Forest evergreen closed](classes/14.md) |  |
| 15 | [Forest deciduous closed](classes/15.md) |  |
| 16 | [Mopane](classes/16.md) |  |
| 17 | [Forest evergreen open](classes/17.md) |  |
| 18 | [Forest deciduous open](classes/18.md) |  |
