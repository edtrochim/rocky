---
id: registry:L23
kind: system
title: Land cover legend for Democratic Rrepublic of Congo
alpha_code: L23
country: Democratic Republic of the Congo
m49: 180
iso3: COD
year: 2021
status: valid
legend_type: LCCS3
format: lccs3
publisher: '-'
reference_link: '-'
reference_file: '-'
n_classes_index: 6
n_classes_file: 6
n_classes_matched: 6
n_datasets: 0
files:
- okf/registry/_raw/L23/L23.csv
- okf/registry/_raw/L23/L23.eapx
- okf/registry/_raw/L23/L23.lccs
- okf/registry/_raw/L23/L23.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L23:WDL
  path: classes/WDL.md
- rel: has_class
  id: registry:L23:GRS
  path: classes/GRS.md
- rel: has_class
  id: registry:L23:CRP
  path: classes/CRP.md
- rel: has_class
  id: registry:L23:BRS
  path: classes/BRS.md
- rel: has_class
  id: registry:L23:ART
  path: classes/ART.md
- rel: has_class
  id: registry:L23:WB
  path: classes/WB.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# Land cover legend for Democratic Rrepublic of Congo

Democratic Republic of the Congo · 2021 · LCCS3 · status valid. Publisher: -. 6 classes in the registry index, 6 in the legend file, 6 matched by code or name.

Reference: - (-), -

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| WDL | [Woodland](classes/WDL.md) | Natural land covered with trees or shrubs (> 10 % canopy cover) |
| GRS | [Grassland](classes/GRS.md) | Natural herbaceous vegetation - close to very open. |
| CRP | [Cropland](classes/CRP.md) | Annual herbaceous crop - irrigated/rainfed. |
| BRS | [Bare soil](classes/BRS.md) | Unconsolidated bare soil. |
| ART | [Artificial surface](classes/ART.md) | Built-up land, including populated places, industrial sites, major roads, and extraction sites. |
| WB | [Water body](classes/WB.md) | Perennial freshwater, natural or artificial |
