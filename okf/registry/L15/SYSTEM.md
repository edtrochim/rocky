---
id: registry:L15
kind: system
title: System of Environmental-Economic Accounting (SEEA) land cover legend
alpha_code: L15
country: Global
m49: 1
iso3: '-'
year: 2014
status: valid
legend_type: LCCS3
format: lccs3
publisher: The United Nations and The European Union
reference_link: https://seea.un.org/sites/seea.un.org/files/seea_cf_final_en.pdf
reference_file: Ref_15.pdf
n_classes_index: 14
n_classes_file: 14
n_classes_matched: 14
n_datasets: 0
files:
- okf/registry/_raw/L15/L15.csv
- okf/registry/_raw/L15/L15.eapx
- okf/registry/_raw/L15/L15.lccs
- okf/registry/_raw/L15/L15.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L15:SEEA-1
  path: classes/SEEA-1.md
- rel: has_class
  id: registry:L15:SEEA-2
  path: classes/SEEA-2.md
- rel: has_class
  id: registry:L15:SEEA-3
  path: classes/SEEA-3.md
- rel: has_class
  id: registry:L15:SEEA-4
  path: classes/SEEA-4.md
- rel: has_class
  id: registry:L15:SEEA-5
  path: classes/SEEA-5.md
- rel: has_class
  id: registry:L15:SEEA-6
  path: classes/SEEA-6.md
- rel: has_class
  id: registry:L15:SEEA-7
  path: classes/SEEA-7.md
- rel: has_class
  id: registry:L15:SEEA-8
  path: classes/SEEA-8.md
- rel: has_class
  id: registry:L15:SEEA-9
  path: classes/SEEA-9.md
- rel: has_class
  id: registry:L15:SEEA-10
  path: classes/SEEA-10.md
- rel: has_class
  id: registry:L15:SEEA-11
  path: classes/SEEA-11.md
- rel: has_class
  id: registry:L15:SEEA-12
  path: classes/SEEA-12.md
- rel: has_class
  id: registry:L15:SEEA-13
  path: classes/SEEA-13.md
- rel: has_class
  id: registry:L15:SEEA-14
  path: classes/SEEA-14.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# System of Environmental-Economic Accounting (SEEA) land cover legend

Global · 2014 · LCCS3 · status valid. Publisher: The United Nations and The European Union. 14 classes in the registry index, 14 in the legend file, 14 matched by code or name.

Reference: System of Environmental-Economic Accounting 2012, Central Framework (2014), https://seea.un.org/sites/seea.un.org/files/seea_cf_final_en.pdf

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| SEEA 1 | [Artificial surfaces (including urban and associated areas)](classes/SEEA-1.md) | The category is composed of any type of artificial surfaces |
| SEEA 2 | [Herbaceous crops](classes/SEEA-2.md) | The category is composed of a main layer of cultivated herbaceous plants. |
| SEEA 3 | [Woody crops](classes/SEEA-3.md) | The category is composed of a main layer of cultivated tree or shrub plants. |
| SEEA 4 | [Multiple or layered crops](classes/SEEA-4.md) | The category is composed of at least two layers of cultivated woody and herbaceous plants or different layers… |
| SEEA 5 | [Grassland](classes/SEEA-5.md) | The category is composed of a main layer of natural herbaceous vegetation with a cover from 10 to 100 per cen… |
| SEEA 6 | [Trees covered areas](classes/SEEA-6.md) | The category is composed of a main layer of natural trees with a cover from 10 to 100 per cent. |
| SEEA 7 | [Mangroves](classes/SEEA-7.md) | The category is composed of natural trees with a cover from 10 to 100 per cent in aquatic or regularly floode… |
| SEEA 8 | [Shrub covered areas](classes/SEEA-8.md) | The category is composed of a main layer of natural shrubs with a cover from 10 to 100 per cent. |
| SEEA 9 | [Shrubs and/or herbaceous vegetation, aquatic or regularly flooded](classes/SEEA-9.md) | The category is composed of natural shrubs or herbs with a cover from 10 to 100 percent in aquatic or regular… |
| SEEA 10 | [Sparsely natural vegetated areas](classes/SEEA-10.md) | The category is composed of any type of natural vegetation (all growth forms) with a cover from 2 to 10 per c… |
| SEEA 11 | [Terrestrial barren land](classes/SEEA-11.md) | The category is composed of abiotic natural surfaces. |
| SEEA 12 | [Permanent snow and glaciers](classes/SEEA-12.md) | The category is composed of abiotic natural surfaces. |
| SEEA 13 | [Inland water bodies](classes/SEEA-13.md) | The category is composed of any type of inland water body with a water persistence of 12 months per year. |
| SEEA 14 | [Coastal water bodies and intertidal areas](classes/SEEA-14.md) | The category is composed on the basis of geographical features in relation to the sea (lagoons and estuaries)… |
