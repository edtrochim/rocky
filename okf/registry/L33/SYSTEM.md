---
id: registry:L33
kind: system
title: Land cover legend for GLC-SHARE
alpha_code: L33
country: Global
m49: 1
iso3: '-'
year: 2014
status: valid
legend_type: LCCS3
format: lccs3
publisher: Food and Agriculture Organization of the United Nations
reference_link: Dominant land cover type (Global - ~1sqkm) GLC-SHARE - Datasets - "FAO catalog"
reference_file: Ref_33.pdf
n_classes_index: 11
n_classes_file: 11
n_classes_matched: 11
n_datasets: 1
files:
- okf/registry/_raw/L33/L33.csv
- okf/registry/_raw/L33/L33.eapx
- okf/registry/_raw/L33/L33.lccs
- okf/registry/_raw/L33/L33.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L33:1
  path: classes/1.md
- rel: has_class
  id: registry:L33:2.1
  path: classes/2.1.md
- rel: has_class
  id: registry:L33:3
  path: classes/3.md
- rel: has_class
  id: registry:L33:4
  path: classes/4.md
- rel: has_class
  id: registry:L33:5
  path: classes/5.md
- rel: has_class
  id: registry:L33:6
  path: classes/6.md
- rel: has_class
  id: registry:L33:7
  path: classes/7.md
- rel: has_class
  id: registry:L33:8
  path: classes/8.md
- rel: has_class
  id: registry:L33:9
  path: classes/9.md
- rel: has_class
  id: registry:L33:10
  path: classes/10.md
- rel: has_class
  id: registry:L33:11
  path: classes/11.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# Land cover legend for GLC-SHARE

Global · 2014 · LCCS3 · status valid. Publisher: Food and Agriculture Organization of the United Nations. 11 classes in the registry index, 11 in the legend file, 11 matched by code or name.

Reference: Global land cover - SHARE (2014), Dominant land cover type (Global - ~1sqkm) GLC-SHARE - Datasets - "FAO catalog"

## Datasets (1)

- Global land cover SHARE, GLC-SHARE (iso/7f4f5ce4-9a3e-406f-bae6-efe63867329a)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| 1 | [Artificial Surfaces](classes/1.md) | The class is composed of any type of areas with a predominant artificial surface.Any urban or related feature… |
| 2.1 | [Cropland](classes/2.1.md) | This class contains three different crop types including Herbaceous Crops, Woody Crops and Multiple or Layere… |
| 3 | [Grassland](classes/3.md) | This class includes any geographic area dominated by natural herbaceous plants (grasslands, prairies, steppes… |
| 4 | [Tree Covered Area](classes/4.md) | This class includes any geographic area dominated by natural tree plants with a cover of 10% or more. Other t… |
| 5 | [Shrubs Covered Area](classes/5.md) | This class includes any geographical area dominated by natural shrubs having a cover of 10% or more. Trees ca… |
| 6 | [Herbaceous vegetation, aquatic or regularly flooded](classes/6.md) | This class includes any geographic area dominated by natural herbaceous vegetation (cover of 10% or more) tha… |
| 7 | [Mangroves](classes/7.md) | This class includes any geographical area dominated by woody vegetation (trees and/or shrubs) with a cover of… |
| 8 | [Sparse vegetation](classes/8.md) | This class includes any geographic areas were the cover of natural vegetation is between 2% and 10%. This inc… |
| 9 | [BareSoil](classes/9.md) | This class includes any geographic area dominated by natural abiotic surfaces (bare soil, sand, rocks, etc.) … |
| 10 | [Snow and glaciers](classes/10.md) | This class includes any geographic area covered by snow or glaciers persistently for 10 months or more. |
| 11 | [Waterbodies](classes/11.md) | This class includes any geographic area covered for most of the year by inland water bodies. In some cases th… |
