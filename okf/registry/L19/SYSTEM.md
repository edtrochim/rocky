---
id: registry:L19
kind: system
title: National land cover legend for Haiti
alpha_code: L19
country: Haiti
m49: 332
iso3: HTI
year: 2010
status: valid
legend_type: LCCS3
format: lccs3
publisher: Food and Agriculture Organization of United Nations
reference_link: haiti-earthquake-map-landuse landcover-FAO.pdf
reference_file: Ref_19.pdf
n_classes_index: 19
n_classes_file: 19
n_classes_matched: 19
n_datasets: 1
files:
- okf/registry/_raw/L19/L19.csv
- okf/registry/_raw/L19/L19.eapx
- okf/registry/_raw/L19/L19.lccs
- okf/registry/_raw/L19/L19.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L19:5UR
  path: classes/5UR.md
- rel: has_class
  id: registry:L19:6S
  path: classes/6S.md
- rel: has_class
  id: registry:L19:8WFP
  path: classes/8WFP.md
- rel: has_class
  id: registry:L19:1Torc
  path: classes/1Torc.md
- rel: has_class
  id: registry:L19:8L
  path: classes/8L.md
- rel: has_class
  id: registry:L19:7L
  path: classes/7L.md
- rel: has_class
  id: registry:L19:2H
  path: classes/2H.md
- rel: has_class
  id: registry:L19:1HM
  path: classes/1HM.md
- rel: has_class
  id: registry:L19:2T
  path: classes/2T.md
- rel: has_class
  id: registry:L19:2SR
  path: classes/2SR.md
- rel: has_class
  id: registry:L19:4H
  path: classes/4H.md
- rel: has_class
  id: registry:L19:2HR
  path: classes/2HR.md
- rel: has_class
  id: registry:L19:4T
  path: classes/4T.md
- rel: has_class
  id: registry:L19:1MC
  path: classes/1MC.md
- rel: has_class
  id: registry:L19:1MixU
  path: classes/1MixU.md
- rel: has_class
  id: registry:L19:1HR
  path: classes/1HR.md
- rel: has_class
  id: registry:L19:2NatVeg
  path: classes/2NatVeg.md
- rel: has_class
  id: registry:L19:1HS_Isol
  path: classes/1HS_Isol.md
- rel: has_class
  id: registry:L19:1HS_Clust
  path: classes/1HS_Clust.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# National land cover legend for Haiti

Haiti · 2010 · LCCS3 · status valid. Publisher: Food and Agriculture Organization of United Nations. 19 classes in the registry index, 19 in the legend file, 19 matched by code or name.

Reference: Haiti- Land cover 2010 (2010), haiti-earthquake-map-landuse landcover-FAO.pdf

## Datasets (1)

- Land cover of Haiti (2010) (iso/a4a257e4-3aa9-4650-a8bb-933cab7682a8)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| 5UR | [Urban areas](classes/5UR.md) | Urban area(s) |
| 6S | [Bare Soil](classes/6S.md) | Bare Soil And/Or Other Unconsolidated Material(s) |
| 8WFP | [River](classes/8WFP.md) | Perennial Natural Waterbodies (Flowing). |
| 1Torc | [Irrigated Orchard](classes/1Torc.md) | Small Sized Field(s) Of Irrigated Tree Crop(s) |
| 8L | [Natural Lakes - Ponds](classes/8L.md) | Natural Waterbodies (Standing). |
| 7L | [Fishponds - Artificial basin](classes/7L.md) | Artificial Waterbodies (Standing). |
| 2H | [Herbaceous vegetation](classes/2H.md) | Herbaceous Closed to Open Vegetation |
| 1HM | [Herbaceous Crop Continuous Medium Fields](classes/1HM.md) | Medium Sized Field(s) Of Herbaceous Crop(s) |
| 2T | [Closed to Opend forest Trees](classes/2T.md) | Closed to Open Trees |
| 2SR | [Closed to Opend Shrubs](classes/2SR.md) | Closed to Open Shrubland (Thicket) |
| 4H | [Closed to Open Natural Acquatic Herbaceous Vegetation](classes/4H.md) | Closed to Open Natural Acquatic Herbaceous Vegetation |
| 2HR | [Sparse Herbaceous Vegetation](classes/2HR.md) | Herbaceous Sparse Vegetation. |
| 4T | [Mangrove](classes/4T.md) | Mangroves are a group of trees and shrubs that live in the coastal intertidal zone. |
| 1MC | [Multiple Crop - Agroforest](classes/1MC.md) | Field(s) Of Tree Crop(s) . |
| 1MixU | [Complex Units](classes/1MixU.md) | Complex units present mainly along the canals formed by Small Sized Field(s) Of Irrigated Tree Crop(s) with P… |
| 1HR | [Herbaceous Crop Fields - Small](classes/1HR.md) | Small Sized Field(s) Of Herbaceous Crop(s). |
| 2NatVeg | [Natural vegetation](classes/2NatVeg.md) | Natural And Semi-Natural Primarily Terrestrial Vegetation. |
| 1HS_Isol | [Agricultural fields Scattered Isolated](classes/1HS_Isol.md) | Scattered Isolated Field(s) Of Herbaceous Crop(s) |
| 1HS_Clust | [Herbaceous crop fields -small clustered](classes/1HS_Clust.md) | Herbaceous Crop Fields -Small Scattered Clustered (20-50% of area). |
