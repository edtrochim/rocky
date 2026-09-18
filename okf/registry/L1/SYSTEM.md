---
id: registry:L1
kind: system
title: Globcover legend
alpha_code: L1
country: Global
m49: 1
iso3: '-'
year: 2009
status: valid
legend_type: LCCS3
format: lccs3
publisher: Food and Agriculture Organization of the United Nations
reference_link: http://due.esrin.esa.int/page_globcover.php
reference_file: Ref_1.pdf
n_classes_index: 23
n_classes_file: 23
n_classes_matched: 22
n_datasets: 60
files:
- okf/registry/_raw/L1/L1.csv
- okf/registry/_raw/L1/L1.eapx
- okf/registry/_raw/L1/L1.lccs
- okf/registry/_raw/L1/L1.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L1:1A
  path: classes/1A.md
- rel: has_class
  id: registry:L1:1B
  path: classes/1B.md
- rel: has_class
  id: registry:L1:14
  path: classes/14.md
- rel: has_class
  id: registry:L1:20
  path: classes/20.md
- rel: has_class
  id: registry:L1:30
  path: classes/30.md
- rel: has_class
  id: registry:L1:40
  path: classes/40.md
- rel: has_class
  id: registry:L1:50
  path: classes/50.md
- rel: has_class
  id: registry:L1:60
  path: classes/60.md
- rel: has_class
  id: registry:L1:70
  path: classes/70.md
- rel: has_class
  id: registry:L1:90
  path: classes/90.md
- rel: has_class
  id: registry:L1:100
  path: classes/100.md
- rel: has_class
  id: registry:L1:110
  path: classes/110.md
- rel: has_class
  id: registry:L1:120
  path: classes/120.md
- rel: has_class
  id: registry:L1:130
  path: classes/130.md
- rel: has_class
  id: registry:L1:140
  path: classes/140.md
- rel: has_class
  id: registry:L1:150
  path: classes/150.md
- rel: has_class
  id: registry:L1:160
  path: classes/160.md
- rel: has_class
  id: registry:L1:170
  path: classes/170.md
- rel: has_class
  id: registry:L1:180
  path: classes/180.md
- rel: has_class
  id: registry:L1:190
  path: classes/190.md
- rel: has_class
  id: registry:L1:200
  path: classes/200.md
- rel: has_class
  id: registry:L1:210
  path: classes/210.md
- rel: has_class
  id: registry:L1:220
  path: classes/220.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# Globcover legend

Global · 2009 · LCCS3 · status valid. Publisher: Food and Agriculture Organization of the United Nations. 23 classes in the registry index, 23 in the legend file, 22 matched by code or name.

Reference: GLOBCOVER 2009, Products description and validation report (2009), http://due.esrin.esa.int/page_globcover.php

## Datasets (60)

- Land cover of Cote d'Ivoire - Globcover (iso/098ab48f-2af1-41df-a69d-d5177e2acec6)
- Land cover of Liberia - Globcover (iso/68f12101-c75a-45d0-9d85-5bb49859040d)
- Land cover of Madagascar - Globcover (iso/ed634129-37b9-40a6-8024-05b0e0b626f0)
- Land cover of Gambia - Globcover (iso/5334bca3-71d6-4f46-8008-06675c5fb70a)
- Land cover of Sierra Leone - Globcover (iso/973fdcbe-c347-47a7-9af7-e2e57729a35b)
- Land cover of Eritrea - Globcover (iso/c1f0e345-8ef1-45a2-a0b3-13e183bf13ff)
- Land cover of Burkina Faso - Globcover (iso/d5acf3e9-5f60-4338-8a7d-4dfe36acb7d0)
- Land cover of Equatorial Guinea - Globcover (iso/bbb85e88-7441-492e-9702-e143ac2d62d3)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| 1A | [Post-flooding](classes/1A.md) | Post- flooding cultivation of herbaceous crops |
| 1B | [Irrigated croplands](classes/1B.md) | Irrigated tree crops / Irrigated shrub crops / Irrigated herbaceous crops |
| 14 | [Rainfed croplands](classes/14.md) | Rainfed shrub crops // Rainfed tree crops // Rainfed herbaceous crops |
| 20 | [Mosaic cropland (50-70%) / vegetation (grassland, shrubland, forest) (20-50%)](classes/20.md) | Cultivated and managed terrestrial areas / Natural and semi-natural primarily terrestrial vegetation |
| 30 | [Mosaic vegetation (grassland, shrubland, forest) (50-70%) / cropland (20-50%)](classes/30.md) | Natural and semi-natural primarily terrestrial vegetation / Cultivated and managed terrestrial areas |
| 40 | [Closed to open (>15%) broadleaved evergreen and/or semi-deciduous forest (>5m)](classes/40.md) | Broadleaved evergreen closed to open trees // Semi-deciduous closed to open trees |
| 50 | [Closed (>40%) broadleaved deciduous forest (>5m)](classes/50.md) | Broadleaved deciduous closed to open (100-40%) trees |
| 60 | [Open (15-40%) broadleaved deciduous forest (>5m)](classes/60.md) | Broadleaved deciduous (40-(20-10)%) woodland |
| 70 | [Closed (>40%) needleleaved evergreen forest (>5m)](classes/70.md) | Needleleaved evergreen closed to open (100-40%) trees |
| 90 | [Open (15-40%) needleleaved deciduous or evergreen forest (>5m)](classes/90.md) | Needleleaved evergreen (40-(20-10)%) woodland // Needleleaved deciduous (40-(20-10)%) woodland |
| 100 | [Closed to open (>15%) mixed broadleaved and needleleaved forest (>5m)](classes/100.md) | Broadleaved closed to open trees / Needleleaved closed to open trees |
| 110 | [Mosaic forest/shrubland (50-70%) / grassland (20-50%)](classes/110.md) | Closed to open trees / Closed to open shrubland (thicket) // Herbaceous closed to open vegetation |
| 120 | [Mosaic grassland (50-70%) / forest/shrubland (20-50%)](classes/120.md) | Closed to open shrubland (thicket) // Herbaceous closed to open vegetation / Closed to open trees |
| 130 | [Closed to open (>15%) shrubland (<5m)](classes/130.md) | Broadleaved closed to open shrubland (thicket) |
| 140 | [Closed to open (>15%) grassland](classes/140.md) | Herbaceous closed to very open vegetation // Closed to open lichens/mosses |
| 150 | [Sparse (>15%) vegetation (woody vegetation, shrubs, grassland)](classes/150.md) | Sparse trees // Herbaceous sparse vegetation // Sparse shrubs |
| 160 | [Closed (>40%) broadleaved forest regularly flooded - fresh water](classes/160.md) | Closed to open (100-40%) broadleaved trees on temporarily flooded land, water quality: fresh water // Closed … |
| 170 | [Closed (>40%) broadleaved semi-deciduous and/or evergreen forest regularly flooded - Saline water](classes/170.md) | Closed to open (100-40%) broadleaved trees on permanently flooded land (with daily variations), water quality… |
| 180 | [Closed to open (>15%) vegetation (grassland, shrubland, woody vegetation) on regularly flooded or waterlogged soil - fresh, brackish or saline water](classes/180.md) | Closed to open shrubs // Closed to open herbaceous vegetation |
| 190 | [Artificial surfaces and associated areas (urban areas >50%)](classes/190.md) | Artificial surfaces and associated areas |
| 200 | [Bare areas](classes/200.md) | Bare areas |
| 210 | [Water bodies](classes/210.md) | Bare areasNatural water bodies // Artificial water bodies |
| 220 | [Permanent snow and ice](classes/220.md) | Artificial perennial snow // Artificial perennial ice // Perennial snow // Perennial ice |
