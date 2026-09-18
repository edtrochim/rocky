---
id: registry:L45
kind: system
title: 2023 land cover for Gambia
alpha_code: L45
country: Gambia (The Gambia)
m49: 270
iso3: GMB
year: 2023
status: valid
legend_type: LCCS3
format: lccs3
publisher: Food and Agriculture Organization of the United Nations
reference_link: https://openknowledge.fao.org/server/api/core/bitstreams/621f4512-68b5-4294-b431-48fae6b3c3bb
reference_file: Ref_45.pdf
n_classes_index: 19
n_classes_file: 19
n_classes_matched: 19
n_datasets: 1
files:
- okf/registry/_raw/L45/L45.csv
- okf/registry/_raw/L45/L45.lccs
- okf/registry/_raw/L45/L45.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L45:Ad
  path: classes/Ad.md
- rel: has_class
  id: registry:L45:Ac
  path: classes/Ac.md
- rel: has_class
  id: registry:L45:FO
  path: classes/FO.md
- rel: has_class
  id: registry:L45:Aro
  path: classes/Aro.md
- rel: has_class
  id: registry:L45:Sa
  path: classes/Sa.md
- rel: has_class
  id: registry:L45:Sar
  path: classes/Sar.md
- rel: has_class
  id: registry:L45:Sh
  path: classes/Sh.md
- rel: has_class
  id: registry:L45:Ml
  path: classes/Ml.md
- rel: has_class
  id: registry:L45:Bi
  path: classes/Bi.md
- rel: has_class
  id: registry:L45:Ahm
  path: classes/Ahm.md
- rel: has_class
  id: registry:L45:Ahms
  path: classes/Ahms.md
- rel: has_class
  id: registry:L45:V
  path: classes/V.md
- rel: has_class
  id: registry:L45:Canh
  path: classes/Canh.md
- rel: has_class
  id: registry:L45:Cih
  path: classes/Cih.md
- rel: has_class
  id: registry:L45:Chi
  path: classes/Chi.md
- rel: has_class
  id: registry:L45:P
  path: classes/P.md
- rel: has_class
  id: registry:L45:Bnl
  path: classes/Bnl.md
- rel: has_class
  id: registry:L45:Bla
  path: classes/Bla.md
- rel: has_class
  id: registry:L45:R
  path: classes/R.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# 2023 land cover for Gambia

Gambia (The Gambia) · 2023 · LCCS3 · status valid. Publisher: Food and Agriculture Organization of the United Nations. 19 classes in the registry index, 19 in the legend file, 19 matched by code or name.

Reference: A framework for monitoring geospatial indicators of the resilience of Organizations for Transformative Smallholder Agriculture project (2024), https://openknowledge.fao.org/server/api/core/bitstreams/621f4512-68b5-4294-b431-48fae6b3c3bb

## Datasets (1)

- 2023 land cover of the Gambia (iso/8169aa3c-5f9b-4244-bfe3-6ee2d9034cf6)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| Ad | [Closed forest](classes/Ad.md) | Lands dominated by trees with a percent cover >70% during the entire year. |
| Ac | [Open forest](classes/Ac.md) | Lands dominated by trees with a percent cover between 20 and 70% during the entire year. |
| FO | [Closed shrubs](classes/FO.md) | Lands with woody vegetation between 2 and 5m tall and with shrub canopy cover >70%. Either evergreen or decid… |
| Aro | [Open shrubs](classes/Aro.md) | Lands with woody vegetation between 2 and 5m tall and with shrub canopy cover between 20 and 70%. Either ever… |
| Sa | [Tree savanna](classes/Sa.md) | Lands with herbaceous types of cover. Tree cover between 4–20%. |
| Sar | [Shrub savanna](classes/Sar.md) | Lands with herbaceous types of cover. Shrub cover between 4–20%. |
| Sh | [Grass savanna](classes/Sh.md) | Lands with herbaceous types of cover. Tree and shrub cover is <4%. |
| Ml | [Mangrove forest](classes/Ml.md) | Coastal forests of stilted shrubs or trees bordering the ocean or coastal estuaries, composed of one or sever… |
| Bi | [Flooded woody](classes/Bi.md) | Lands with permanent mixture of freshwater with dominant woody vegetation. |
| Ahm | [Salt marsh](classes/Ahm.md) | Herbaceous or aquatic vegetation in permanent or semi-permanent wetlands and swamps. |
| Ahms | [Swamps](classes/Ahms.md) | Herbaceous or aquatic vegetation in permanent or semi-permanent wetlands and swamps. Water salinity is bracki… |
| V | [Orchards](classes/V.md) | Lands covered with perennial rainfed woody crops land cover type. |
| Canh | [Annual herb cultivation](classes/Canh.md) | Lands covered with temporary rainfed herbaceous crops followed by harvest and a bare soil period. |
| Cih | [Herbaceous crop dominated](classes/Cih.md) | Cultivated agriculture with irrigated area where the growth form herb is dominant. |
| Chi | [Paddy rice](classes/Chi.md) | Cultivated agriculture with flooded area where the growth form herb is dominant. Floristic aspect species: Ri… |
| P | [Beaches](classes/P.md) | Beach sand or shifting mounds of sand, formed by wind; active dunes. |
| Bnl | [Built-up non linear](classes/Bnl.md) | Land covered by buildings and other man-made structures. |
| Bla | [Built-up linear and barren](classes/Bla.md) | Artificial surface where linear elements / Lands with exposed soil, sand, rocks, or snow and never have more … |
| R | [Rivers](classes/R.md) | Flowing fresh water whose persistence is more than 9 months per year. |
