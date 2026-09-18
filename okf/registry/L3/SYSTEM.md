---
id: registry:L3
kind: system
title: Land cover legend for Zanjan Province, Iran
alpha_code: L3
country: Iran (Islamic Republic of)
m49: 364
iso3: IRN
year: 2019
status: valid
legend_type: LCCS3
format: lccs3
publisher: Food and Agriculture Organization of the United Nations
reference_link: http://www.fao.org/geospatial/resources/detail/en/c/1254753/
reference_file: Ref_3.pdf
n_classes_index: 18
n_classes_file: 18
n_classes_matched: 18
n_datasets: 3
files:
- okf/registry/_raw/L3/L3.csv
- okf/registry/_raw/L3/L3.eapx
- okf/registry/_raw/L3/L3.lccs
- okf/registry/_raw/L3/L3.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L3:BA
  path: classes/BA.md
- rel: has_class
  id: registry:L3:FC
  path: classes/FC.md
- rel: has_class
  id: registry:L3:FO
  path: classes/FO.md
- rel: has_class
  id: registry:L3:GRWS
  path: classes/GRWS.md
- rel: has_class
  id: registry:L3:HCI
  path: classes/HCI.md
- rel: has_class
  id: registry:L3:HCR
  path: classes/HCR.md
- rel: has_class
  id: registry:L3:IA
  path: classes/IA.md
- rel: has_class
  id: registry:L3:MN
  path: classes/MN.md
- rel: has_class
  id: registry:L3:RB
  path: classes/RB.md
- rel: has_class
  id: registry:L3:RC
  path: classes/RC.md
- rel: has_class
  id: registry:L3:RD
  path: classes/RD.md
- rel: has_class
  id: registry:L3:TCP
  path: classes/TCP.md
- rel: has_class
  id: registry:L3:UA
  path: classes/UA.md
- rel: has_class
  id: registry:L3:UAM
  path: classes/UAM.md
- rel: has_class
  id: registry:L3:WB
  path: classes/WB.md
- rel: has_class
  id: registry:L3:WET
  path: classes/WET.md
- rel: has_class
  id: registry:L3:FS
  path: classes/FS.md
- rel: has_class
  id: registry:L3:SHTS
  path: classes/SHTS.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# Land cover legend for Zanjan Province, Iran

Iran (Islamic Republic of) · 2019 · LCCS3 · status valid. Publisher: Food and Agriculture Organization of the United Nations. 18 classes in the registry index, 18 in the legend file, 18 matched by code or name.

Reference: Improved Agriculture Monitoring Systems through Satellite Imagery for Iran (2019), http://www.fao.org/geospatial/resources/detail/en/c/1254753/

## Datasets (3)

- Land cover map South Kerman region - The Islamic republic of Iran (no GeoNetwork id)
- Land cover map Zanjan province - The Islamic republic of Iran (no GeoNetwork id)
- Land cover map Mazandaran province - The Islamic republic of Iran (no GeoNetwork id)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| BA | [Bare Area](classes/BA.md) | Rock or Soil sometimes with very sparse natural vegetation (0-15%) |
| FC | [Forest Closed](classes/FC.md) | Woodland with closed (60-100%) trees and/or shrubs |
| FO | [Forest Open](classes/FO.md) | Woodland with open (20-60%) trees and/or shrubs and herbaceous natural vegetation |
| GRWS | [Grassland](classes/GRWS.md) | Relatively dense grassland natural vegetation, with very sparse shrubs and/or trees (0-15%) |
| HCI | [Irrigated Agriculture](classes/HCI.md) | Irrigated herbaceous crops |
| HCR | [Rainfed Agriculture](classes/HCR.md) | Rain-fed herbaceous crops |
| IA | [Industrial Area](classes/IA.md) | Non-urban build-up areas and other constructions (industrial etc...) |
| MN | [Mines](classes/MN.md) | Extractions sites |
| RB | [River Bank](classes/RB.md) | River bank (bare soil) |
| RC | [Rice Crop](classes/RC.md) | Irrigated rice crop |
| RD | [Roads](classes/RD.md) | Roads |
| TCP | [Orchard and other Plantation](classes/TCP.md) | Orchard crops or other plantation |
| UA | [Urban area](classes/UA.md) | Urban and/or rural settlement |
| UAM | [Urban area mixed](classes/UAM.md) | Urban build-up areas + small cultivated herbaceous crops + orchards and other plantations |
| WB | [Water Body](classes/WB.md) | Perennial fresh water lake or river |
| WET | [Wetland](classes/WET.md) | Wetlands are areas where water covers the soil, or is present either at or near the surface of the soil all y… |
| FS | [Forest Sparse](classes/FS.md) | Woodland with sparse (<20%) trees and/or shrubs and herbaceous natural vegetation |
| SHTS | [Shrubland](classes/SHTS.md) | Vegetation dominated by bushes; Natural shrubland vegetation, occasionally with sparse or closed herbaceous |
