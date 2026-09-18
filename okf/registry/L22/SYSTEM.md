---
id: registry:L22
kind: system
title: Central African Forest Innitiative land cover legend
alpha_code: L22
country: Regional
m49: 17
iso3: '-'
year: 2021
status: valid
legend_type: LCCS3
format: lccs3
publisher: Food and Agriculture Organization of United Nations
reference_link: ''
reference_file: Ref_22.pdf
n_classes_index: 19
n_classes_file: 19
n_classes_matched: 11
n_datasets: 0
files:
- okf/registry/_raw/L22/L22.csv
- okf/registry/_raw/L22/L22.eapx
- okf/registry/_raw/L22/L22.lccs
- okf/registry/_raw/L22/L22.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L22:1
  path: classes/1.md
- rel: has_class
  id: registry:L22:2
  path: classes/2.md
- rel: has_class
  id: registry:L22:3
  path: classes/3.md
- rel: has_class
  id: registry:L22:4
  path: classes/4.md
- rel: has_class
  id: registry:L22:5
  path: classes/5.md
- rel: has_class
  id: registry:L22:6
  path: classes/6.md
- rel: has_class
  id: registry:L22:7
  path: classes/7.md
- rel: has_class
  id: registry:L22:8
  path: classes/8.md
- rel: has_class
  id: registry:L22:9
  path: classes/9.md
- rel: has_class
  id: registry:L22:10
  path: classes/10.md
- rel: has_class
  id: registry:L22:11
  path: classes/11.md
- rel: has_class
  id: registry:L22:12
  path: classes/12.md
- rel: has_class
  id: registry:L22:13
  path: classes/13.md
- rel: has_class
  id: registry:L22:14
  path: classes/14.md
- rel: has_class
  id: registry:L22:15
  path: classes/15.md
- rel: has_class
  id: registry:L22:16
  path: classes/16.md
- rel: has_class
  id: registry:L22:17
  path: classes/17.md
- rel: has_class
  id: registry:L22:18
  path: classes/18.md
- rel: has_class
  id: registry:L22:19
  path: classes/19.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# Central African Forest Innitiative land cover legend

Regional · 2021 · LCCS3 · status valid. Publisher: Food and Agriculture Organization of United Nations. 19 classes in the registry index, 19 in the legend file, 11 matched by code or name.

Reference: Estimation of deforestation and degradation of forests and direct current and historical factors associated with these processes using SEPAL (2021), 

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| 1 | [Dense forest](classes/1.md) | Dense primary rainforest on dry land, >60% tree cover |
| 2 | [Dense dry forest](classes/2.md) | Dense forest, 30-60% tree cover with drier seasons |
| 3 | [Secondary forest](classes/3.md) | Opened forest 30-60% tree cover, degraded or secondary |
| 4 | [Dry open forest](classes/4.md) | Dry open forest 30-60% tree cover, with dry seasons |
| 5 | [Sub-montane forest](classes/5.md) | Forest >30% tree cover, 1100-1750m altitude |
| 6 | [Montane forest](classes/6.md) | Forest >30% tree cover, >1750m altitude |
| 7 | [Mangrove](classes/7.md) | Forest >30% tree cover, hydromorphic soil |
| 8 | [Swamp forest](classes/8.md) | Mixed swamp forest >30% tree cover, flooded soil >9 months |
| 9 | [Gallery forest](classes/9.md) | Riparian forest at the bottom of a valley or on the edge of a river |
| 10 | [Mature forest plantation](classes/10.md) | Tree cover> 15% Cultivated / managed vegetation |
| 11 | [Woodland savanna](classes/11.md) | Wooded savannah 15-30% trees and shrubs> national definition |
| 12 | [Mature shrubland savanna](classes/12.md) | Savannah> 15% shrub> national definition |
| 13 | [Shrubland savanna](classes/13.md) | Savannah >15% shrub < national definition |
| 14 | [Grassland savanna](classes/14.md) | Savannah> 15% shrub <national definition |
| 15 | [Aquatic grassland](classes/15.md) | Herbaceous savannah <15% shrub or tree |
| 16 | [Bare land and sparse vegetation](classes/16.md) | Aquatic or regularly flooded herbaceous cover |
| 17 | [Cultivated areas](classes/17.md) | <15% vegetation |
| 18 | [Built-up areas](classes/18.md) | Cultivated shrub cover> 15% shrub / herbaceous / tree |
| 19 | [Water](classes/19.md) | Water > 50% |
