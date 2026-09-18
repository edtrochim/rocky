---
id: registry:L13
kind: system
title: National land cover legend for Cuba
alpha_code: L13
country: Cuba
m49: 192
iso3: CUB
year: 2005
status: valid
legend_type: LCCS3
format: lccs3
publisher: Food and Agriculture Organization of the United Nations
reference_link: '-'
reference_file: Ref_13.pdf
n_classes_index: 19
n_classes_file: 19
n_classes_matched: 19
n_datasets: 1
files:
- okf/registry/_raw/L13/L13.csv
- okf/registry/_raw/L13/L13.eapx
- okf/registry/_raw/L13/L13.lccs
- okf/registry/_raw/L13/L13.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L13:AGt
  path: classes/AGt.md
- rel: has_class
  id: registry:L13:TP
  path: classes/TP.md
- rel: has_class
  id: registry:L13:TSt
  path: classes/TSt.md
- rel: has_class
  id: registry:L13:SSt
  path: classes/SSt.md
- rel: has_class
  id: registry:L13:HSt
  path: classes/HSt.md
- rel: has_class
  id: registry:L13:TCOt
  path: classes/TCOt.md
- rel: has_class
  id: registry:L13:SCOt
  path: classes/SCOt.md
- rel: has_class
  id: registry:L13:HCOt
  path: classes/HCOt.md
- rel: has_class
  id: registry:L13:AGa
  path: classes/AGa.md
- rel: has_class
  id: registry:L13:TSa
  path: classes/TSa.md
- rel: has_class
  id: registry:L13:SSa
  path: classes/SSa.md
- rel: has_class
  id: registry:L13:HSa
  path: classes/HSa.md
- rel: has_class
  id: registry:L13:TCOa
  path: classes/TCOa.md
- rel: has_class
  id: registry:L13:SCOa
  path: classes/SCOa.md
- rel: has_class
  id: registry:L13:HCOa
  path: classes/HCOa.md
- rel: has_class
  id: registry:L13:URB
  path: classes/URB.md
- rel: has_class
  id: registry:L13:BS
  path: classes/BS.md
- rel: has_class
  id: registry:L13:WA
  path: classes/WA.md
- rel: has_class
  id: registry:L13:WN
  path: classes/WN.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# National land cover legend for Cuba

Cuba · 2005 · LCCS3 · status valid. Publisher: Food and Agriculture Organization of the United Nations. 19 classes in the registry index, 19 in the legend file, 19 matched by code or name.

Reference: Cuba land cover mapping and change Assessment (2005), -

## Datasets (1)

- Land cover of Cuba (iso/c9822f6b-5f15-4a05-96a7-b3c15c11fb5c)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| AGt | [Cultivated and Managed Terrestrial Area(s)](classes/AGt.md) | It referred to any type of herbaceous and shrub cropping activities as well as to any irrigation practices. |
| TP | [Tree Plantation](classes/TP.md) | Tree crops or planted trees. |
| TSt | [Sparse Trees (terrestrial)](classes/TSt.md) | Sparse (1-15%) trees in terrestrial environment |
| SSt | [Sparse Shrubs (terrestrial)](classes/SSt.md) | Sparse shrub vegetation in terrestrial environment and coverage percentage is lower than 15%. |
| HSt | [Herbaceous Sparse Vegetation (terrestrial)](classes/HSt.md) | Sparse herbaceous vegetation in terrestrial environment and coverage percentage is lower than 15% |
| TCOt | [Closed to Open Trees](classes/TCOt.md) | Closed to open (15-100% of coverage) forest. |
| SCOt | [Closed to Open Shrubland (Thicket)](classes/SCOt.md) | This classes indicates scrublands areas and shrubs coverage ranges from 15 to 100 %. |
| HCOt | [Herbaceous Closed to Open Vegetation](classes/HCOt.md) | It refers to natural herbaceous vegetation with a coverage percentage ranging from 15 to 100%. |
| AGa | [Cultivated Aquatic or Regularly Flooded Area(s)](classes/AGa.md) | Small sized ( < 2 Ha) fields of rice flooded for more than 9 months. |
| TSa | [Sparse Trees.(acquatic)](classes/TSa.md) | Sparse (<15%) trees in flooded environments. |
| SSa | [Sparse Shrubs (acquatic)](classes/SSa.md) | Sparse (<15%) shrubs in flooded environments. |
| HSa | [Sparse Herbaceous Vegetation (acquatic)](classes/HSa.md) | Sparse (<15%) herbaceous in flooded environments. |
| TCOa | [Closed to Open Trees (acquatic)](classes/TCOa.md) | Closed to open (15-100%) trees in flooded environments. |
| SCOa | [Closed to Open Shrubs (acquatic)](classes/SCOa.md) | Closed to open (15-100%) shrubs in flooded environments. |
| HCOa | [Closed to Open Herbaceous Vegetation.](classes/HCOa.md) | Closed to open (15-100%) herbaceous in flooded environments. |
| URB | [Urban Area(s)](classes/URB.md) | Refers to any artificial surfaces (urban, industrial, eTc.) |
| BS | [Bare Rocks and Soil and/or Other Unconsolidated Material(s)](classes/BS.md) | This class consists of bare areas including quarries. |
| WA | [Artificial Waterbodies](classes/WA.md) | An artificially-created body of water, by damming a source. Often used for flood control, as a drinking water… |
| WN | [Natural Waterbodies](classes/WN.md) | Natural body of water including rivers, ocean, spring, stream, pond, lake, or wetland that was historically p… |
