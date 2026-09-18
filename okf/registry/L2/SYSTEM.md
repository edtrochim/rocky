---
id: registry:L2
kind: system
title: Himalaya region land cover legend
alpha_code: L2
country: Regional
m49: 35
iso3: '-'
year: 2005
status: valid
legend_type: LCCS3
format: lccs3
publisher: Food and Agriculture Organization of the United Nations
reference_link: https://www.un-spider.org/links-and-resources/data-sources/land-cover-and-land-cover-change-himalaya-region-fao
reference_file: Ref_2.pdf
n_classes_index: 35
n_classes_file: 35
n_classes_matched: 35
n_datasets: 12
files:
- okf/registry/_raw/L2/L2.csv
- okf/registry/_raw/L2/L2.eapx
- okf/registry/_raw/L2/L2.lccs
- okf/registry/_raw/L2/L2.xsd
vocabulary:
  errors: 2
  warnings: 2
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L2:1H
  path: classes/1H.md
- rel: has_class
  id: registry:L2:1HI
  path: classes/1HI.md
- rel: has_class
  id: registry:L2:1T
  path: classes/1T.md
- rel: has_class
  id: registry:L2:1S
  path: classes/1S.md
- rel: has_class
  id: registry:L2:1HSs
  path: classes/1HSs.md
- rel: has_class
  id: registry:L2:1HLMv
  path: classes/1HLMv.md
- rel: has_class
  id: registry:L2:1HSv
  path: classes/1HSv.md
- rel: has_class
  id: registry:L2:2HCO
  path: classes/2HCO.md
- rel: has_class
  id: registry:L2:2HS
  path: classes/2HS.md
- rel: has_class
  id: registry:L2:2HS-6BR
  path: classes/2HS-6BR.md
- rel: has_class
  id: registry:L2:2HCO-1H
  path: classes/2HCO-1H.md
- rel: has_class
  id: registry:L2:2SCO
  path: classes/2SCO.md
- rel: has_class
  id: registry:L2:2SS
  path: classes/2SS.md
- rel: has_class
  id: registry:L2:2SSd
  path: classes/2SSd.md
- rel: has_class
  id: registry:L2:2SOd
  path: classes/2SOd.md
- rel: has_class
  id: registry:L2:2TCOne-2TCObe
  path: classes/2TCOne-2TCObe.md
- rel: has_class
  id: registry:L2:2TCOne
  path: classes/2TCOne.md
- rel: has_class
  id: registry:L2:2TCObe
  path: classes/2TCObe.md
- rel: has_class
  id: registry:L2:2TSne-2TSbe
  path: classes/2TSne-2TSbe.md
- rel: has_class
  id: registry:L2:2TSne
  path: classes/2TSne.md
- rel: has_class
  id: registry:L2:2TSbe
  path: classes/2TSbe.md
- rel: has_class
  id: registry:L2:4HCOp
  path: classes/4HCOp.md
- rel: has_class
  id: registry:L2:4SCOs
  path: classes/4SCOs.md
- rel: has_class
  id: registry:L2:5UI
  path: classes/5UI.md
- rel: has_class
  id: registry:L2:6BR
  path: classes/6BR.md
- rel: has_class
  id: registry:L2:6S
  path: classes/6S.md
- rel: has_class
  id: registry:L2:6GR
  path: classes/6GR.md
- rel: has_class
  id: registry:L2:8ICE
  path: classes/8ICE.md
- rel: has_class
  id: registry:L2:8ICEr
  path: classes/8ICEr.md
- rel: has_class
  id: registry:L2:8SN
  path: classes/8SN.md
- rel: has_class
  id: registry:L2:8SNs
  path: classes/8SNs.md
- rel: has_class
  id: registry:L2:8WNP
  path: classes/8WNP.md
- rel: has_class
  id: registry:L2:8WBS
  path: classes/8WBS.md
- rel: has_class
  id: registry:L2:8WP
  path: classes/8WP.md
- rel: has_class
  id: registry:L2:8WF
  path: classes/8WF.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# Himalaya region land cover legend

Regional · 2005 · LCCS3 · status valid. Publisher: Food and Agriculture Organization of the United Nations. 35 classes in the registry index, 35 in the legend file, 35 matched by code or name.

Reference: Regional Workshop on development & harmonization of land cover classification in the HKH Region (2008), https://www.un-spider.org/links-and-resources/data-sources/land-cover-and-land-cover-change-himalaya-region-fao

## Datasets (12)

- Land cover map of Afghanistan - Himalaya region (iso/46d3c2ef-72c3-4f96-8e32-40723cd1847b)
- Land cover map of Bhutan - Himalaya region (iso/46d3c2ef-72c3-4f96-8e32-40723cd1847b)
- Land cover map of Yunnan Sheng - Himalaya region (iso/46d3c2ef-72c3-4f96-8e32-40723cd1847b)
- Land cover map of Xizang Zizhiqu - Himalaya region (iso/46d3c2ef-72c3-4f96-8e32-40723cd1847b)
- Land cover map of China-India - Himalaya region (iso/46d3c2ef-72c3-4f96-8e32-40723cd1847b)
- Land cover map of Aksai Chin - Himalaya region (iso/46d3c2ef-72c3-4f96-8e32-40723cd1847b)
- Land cover map of Myanmar - Himalaya region (iso/46d3c2ef-72c3-4f96-8e32-40723cd1847b)
- Land cover map of Nepal - Himalaya region (iso/46d3c2ef-72c3-4f96-8e32-40723cd1847b)

## Vocabulary check of the registry file

2 errors, 2 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| 1H | [Rainfed herbaceos crop](classes/1H.md) | Rainfed herbaceos crop |
| 1HI | [Irrigated herbaceous crops](classes/1HI.md) | Irrigated herbaceous crops |
| 1T | [Tree crop](classes/1T.md) | Tree crop |
| 1S | [Tea crop](classes/1S.md) | Orchards of tea crops |
| 1HSs | [Small herbaceous crops in sloping land](classes/1HSs.md) | Small (< 2 ha) herbaceous crops in sloping land |
| 1HLMv | [Large to medium herbaceous crops in valley floor](classes/1HLMv.md) | Large to medium (> 2 ha) herbaceous crops in valley floor |
| 1HSv | [Small herbaceous crops in valley floor](classes/1HSv.md) | Small (< 2 ha) herbaceous crops in valley floor |
| 2HCO | [Closed to open herbaceous](classes/2HCO.md) | Closed to Open (15-100%) herbaceous vegetation |
| 2HS | [Sparse herbaceous](classes/2HS.md) | Sparse (1-15%) short herbaceous vegetation |
| 2HS//6BR | [Sparse herbaceous or Bare rock](classes/2HS-6BR.md) | Sparse (1-15%) short herbaceous vegetation or Bare rock |
| 2HCO//1H | [Closed to open herbaceous or Rainfed herbaceous crops](classes/2HCO-1H.md) | Closed to Open (15-100%) herbaceous vegetation or Rainfed herbaceous crop |
| 2SCO | [Closed to open shrubs](classes/2SCO.md) | Closed to Open (15-100%) medium high shrubs |
| 2SS | [Sparse shrubs with sparse herbaceous](classes/2SS.md) | Sparse (1-15%) shrubs with sparse (1-15%) herbaceous |
| 2SSd | [Sparse dwarf shrubs with sparse herbaceous](classes/2SSd.md) | Sparse (1-15%) dwarf (< 0,5 m) shrubs with sparse (1-15%) herbaceous |
| 2SOd | [Open dwarf shrubs with sparse herbaceous](classes/2SOd.md) | Open (15-65 %) dwarf shrubs with open (15-100%) herbaceous |
| 2TCOne//2TCObe | [Closed to open needleleaved trees or closed to open broadleaved trees](classes/2TCOne-2TCObe.md) | Trees closed to open (15-100%), needleleaved evergreen or Trees closed to open (15-100%), broadleaved evergre… |
| 2TCOne | [Closed to open needleleaved trees](classes/2TCOne.md) | Trees closed to open (15-100%), needleaved evergreen |
| 2TCObe | [Closed to open broadleaved trees](classes/2TCObe.md) | Trees closed to open (15-100%), broadleaved evergreen |
| 2TSne//2TSbe | [Sparse needleleaved trees or Sparse broadleaved trees](classes/2TSne-2TSbe.md) | Trees sparse (1-15%), needleleaved evergreen or Trees sparse (1-15%), broadleaved evergreen |
| 2TSne | [Sparse needleleaved trees](classes/2TSne.md) | Sparse (1-15%) needleleaved evergreen trees |
| 2TSbe | [Sparse broadleaved trees](classes/2TSbe.md) | Trees sparse (1-15%), broadleaved evergreen |
| 4HCOp | [Closed to open permanently flooded herbaceous](classes/4HCOp.md) | Closed to open (15-100%) herbaceous vegetation on flooded land (> 4 months) |
| 4SCOs | [Closed to open seasonally flooded shrubs](classes/4SCOs.md) | Closed to open (15-100%) shrubs in temporarily flooded land (2-4 months) |
| 5UI | [Urban and industrial areas](classes/5UI.md) | Urban and industrial areas |
| 6BR | [Bare rock](classes/6BR.md) | Bare rock |
| 6S | [Bare soil](classes/6S.md) | Unconsolidated bare soil |
| 6GR | [Rock debris](classes/6GR.md) | River banks and rock debries |
| 8ICE | [Glacier](classes/8ICE.md) | Glacier |
| 8ICEr | [Rocky glacier](classes/8ICEr.md) | Glacier covered by rock debris |
| 8SN | [Perennial snow](classes/8SN.md) | Perennial snow (> 9 months) |
| 8SNs | [Seasonal snow](classes/8SNs.md) | Seasonal snow (< 9 months) |
| 8WNP | [Non-Perennial lakes](classes/8WNP.md) | Non-Perennial (< 9 months) lakes |
| 8WBS | [Bare soil in seasonally flooded area](classes/8WBS.md) | Bare soil seasonally flooded (water presence: 1-3 months) |
| 8WP | [Lakes](classes/8WP.md) | Lakes |
| 8WF | [Rivers](classes/8WF.md) | Rivers |
