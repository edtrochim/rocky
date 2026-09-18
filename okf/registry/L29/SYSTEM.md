---
id: registry:L29
kind: system
title: Land cover legend of Nepal
alpha_code: L29
country: Nepal
m49: 524
iso3: NPL
year: 2019
status: valid
legend_type: LCCS3
format: lccs3
publisher: International Centre for Integrated Mountain Development
reference_link: ''
reference_file: Ref_29.pdf
n_classes_index: 11
n_classes_file: 11
n_classes_matched: 11
n_datasets: 1
files:
- okf/registry/_raw/L29/L29.csv
- okf/registry/_raw/L29/L29.eapx
- okf/registry/_raw/L29/L29.lccs
- okf/registry/_raw/L29/L29.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L29:lcc1
  path: classes/lcc1.md
- rel: has_class
  id: registry:L29:lcc2
  path: classes/lcc2.md
- rel: has_class
  id: registry:L29:lcc3
  path: classes/lcc3.md
- rel: has_class
  id: registry:L29:lcc4
  path: classes/lcc4.md
- rel: has_class
  id: registry:L29:lcc5
  path: classes/lcc5.md
- rel: has_class
  id: registry:L29:lcc6
  path: classes/lcc6.md
- rel: has_class
  id: registry:L29:lcc7
  path: classes/lcc7.md
- rel: has_class
  id: registry:L29:lcc8
  path: classes/lcc8.md
- rel: has_class
  id: registry:L29:lcc9
  path: classes/lcc9.md
- rel: has_class
  id: registry:L29:lcc10
  path: classes/lcc10.md
- rel: has_class
  id: registry:L29:lcc11
  path: classes/lcc11.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# Land cover legend of Nepal

Nepal · 2019 · LCCS3 · status valid. Publisher: International Centre for Integrated Mountain Development. 11 classes in the registry index, 11 in the legend file, 11 matched by code or name.

Reference: Land cover of Nepal (2019), 

## Datasets (1)

- National land cover map of Nepal (https://rds.icimod.org/metadata/073f1390-3b0e-4320-8446-8466ad118c59)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| lcc1 | [Forest](classes/lcc1.md) | Land spanning more than 0.5 ha with trees higher than 5 m and a canopy cover of more than 10%, or trees able … |
| lcc2 | [Cropland](classes/lcc2.md) | This category includes arable and tillage land, and agroforestry systems where vegetation falls below the thr… |
| lcc3 | [Built-up](classes/lcc3.md) | Built-up areas refer to artificial structures such as towns, villages, industrial areas, airports, etc. |
| lcc4 | [Water bodies](classes/lcc4.md) | Rivers are natural flowing water bodies and typically have elongated shapes. Lakes and ponds are perennial st… |
| lcc5 | [Other wooded land](classes/lcc5.md) | Land not classified as forest spanning more than 0.5 ha, having at least 20 m width and a tree canopy cover o… |
| lcc6 | [Glacier](classes/lcc6.md) | Perennial ice in movement. |
| lcc7 | [Bare rock](classes/lcc7.md) | Non-vegetated areas with a rock surface. |
| lcc8 | [Grassland](classes/lcc8.md) | Areas covered by herbaceous vegetation with cover ranging from Closed to Open (15–100%). This category includ… |
| lcc9 | [Snow](classes/lcc9.md) | This class describes perennial snow (persistence > 9 months per year). |
| lcc10 | [Bare soil](classes/lcc10.md) | A soil surface devoid of any plant material. |
| lcc11 | [Riverbed](classes/lcc11.md) | A tract of land without vegetation surrounded by the waters of an ocean, lake, or stream; it usually includes… |
