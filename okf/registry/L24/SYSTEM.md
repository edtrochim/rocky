---
id: registry:L24
kind: system
title: National land cover legend for Sudan
alpha_code: L24
country: Sudan
m49: 729
iso3: SDN
year: 2020
status: valid
legend_type: LCCS3
format: lccs3
publisher: Food and Agriculture Organization of United Nations
reference_link: https://www.humanitarianresponse.info/fr/operations/sudan/document/republic-sudan-national-land-cover-map-2020-report
reference_file: Ref_24.pdf
n_classes_index: 7
n_classes_file: 7
n_classes_matched: 7
n_datasets: 1
files:
- okf/registry/_raw/L24/L24.csv
- okf/registry/_raw/L24/L24.eapx
- okf/registry/_raw/L24/L24.lccs
- okf/registry/_raw/L24/L24.xsd
vocabulary:
  errors: 2
  warnings: 1
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L24:AG
  path: classes/AG.md
- rel: has_class
  id: registry:L24:BS
  path: classes/BS.md
- rel: has_class
  id: registry:L24:TCO
  path: classes/TCO.md
- rel: has_class
  id: registry:L24:HCO
  path: classes/HCO.md
- rel: has_class
  id: registry:L24:SCO
  path: classes/SCO.md
- rel: has_class
  id: registry:L24:URB
  path: classes/URB.md
- rel: has_class
  id: registry:L24:WAT
  path: classes/WAT.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# National land cover legend for Sudan

Sudan · 2020 · LCCS3 · status valid. Publisher: Food and Agriculture Organization of United Nations. 7 classes in the registry index, 7 in the legend file, 7 matched by code or name.

Reference: National land cover map for Republic of Sudan (2020), https://www.humanitarianresponse.info/fr/operations/sudan/document/republic-sudan-national-land-cover-map-2020-report

## Datasets (1)

- National land cover map of Sudan (2020) (iso/3d2d745c-320b-44f8-a301-c058cfd0f7f5)

## Vocabulary check of the registry file

2 errors, 1 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| AG | [Agriculture](classes/AG.md) | Agriculture in terrestrial and aquatic/regularly flooded land. |
| BS | [Bare rocks and soils](classes/BS.md) | Bare rocks and soils and/or other unconsolidated material(s). |
| TCO | [Forest](classes/TCO.md) | Trees closed-to-sparse in terrestrial and aquatic/regularly flooded land. |
| HCO | [Herbaceous](classes/HCO.md) | Herbaceous closed-to-sparse in terrestrial and aquatic/regularly flooded land. |
| SCO | [Shrubs](classes/SCO.md) | Shrubs closed-to-sparse in terrestrial and aquatic/regularly flooded land. |
| URB | [Urban areas](classes/URB.md) | Urban areas |
| WAT | [Water bodies](classes/WAT.md) | Seasonal/perennial, natural/artificial Water bodies. |
