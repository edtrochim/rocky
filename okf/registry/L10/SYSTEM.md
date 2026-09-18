---
id: registry:L10
kind: system
title: National land cover legend for Afghanistan
alpha_code: L10
country: Afghanistan
m49: 4
iso3: AFG
year: 2010
status: valid
legend_type: LCCS3
format: lccs3
publisher: Food and Agriculture Organization of the United Nations
reference_link: http://www.fao.org/geospatial/resources/detail/en/c/1024570/
reference_file: Ref_10.pdf
n_classes_index: 29
n_classes_file: 27
n_classes_matched: 26
n_datasets: 1
files:
- okf/registry/_raw/L10/L10.csv
- okf/registry/_raw/L10/L10.eapx
- okf/registry/_raw/L10/L10.lccs
- okf/registry/_raw/L10/L10.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L10:1A
  path: classes/1A.md
- rel: has_class
  id: registry:L10:1B
  path: classes/1B.md
- rel: has_class
  id: registry:L10:2A
  path: classes/2A.md
- rel: has_class
  id: registry:L10:2B
  path: classes/2B.md
- rel: has_class
  id: registry:L10:3A-1
  path: classes/3A-1.md
- rel: has_class
  id: registry:L10:3A-2
  path: classes/3A-2.md
- rel: has_class
  id: registry:L10:3A
  path: classes/3A.md
- rel: has_class
  id: registry:L10:3A1-1
  path: classes/3A1-1.md
- rel: has_class
  id: registry:L10:3A1-2
  path: classes/3A1-2.md
- rel: has_class
  id: registry:L10:3A1
  path: classes/3A1.md
- rel: has_class
  id: registry:L10:3B
  path: classes/3B.md
- rel: has_class
  id: registry:L10:3C
  path: classes/3C.md
- rel: has_class
  id: registry:L10:4A
  path: classes/4A.md
- rel: has_class
  id: registry:L10:4B
  path: classes/4B.md
- rel: has_class
  id: registry:L10:6A
  path: classes/6A.md
- rel: has_class
  id: registry:L10:6B
  path: classes/6B.md
- rel: has_class
  id: registry:L10:6B1
  path: classes/6B1.md
- rel: has_class
  id: registry:L10:6C
  path: classes/6C.md
- rel: has_class
  id: registry:L10:7
  path: classes/7.md
- rel: has_class
  id: registry:L10:8A
  path: classes/8A.md
- rel: has_class
  id: registry:L10:8B
  path: classes/8B.md
- rel: has_class
  id: registry:L10:8C
  path: classes/8C.md
- rel: has_class
  id: registry:L10:9A
  path: classes/9A.md
- rel: has_class
  id: registry:L10:9B
  path: classes/9B.md
- rel: has_class
  id: registry:L10:10A
  path: classes/10A.md
- rel: has_class
  id: registry:L10:10B
  path: classes/10B.md
- rel: has_class
  id: registry:L10:11
  path: classes/11.md
- rel: has_class
  id: registry:L10:12
  path: classes/12.md
- rel: has_class
  id: registry:L10:13
  path: classes/13.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# National land cover legend for Afghanistan

Afghanistan · 2010 · LCCS3 · status valid. Publisher: Food and Agriculture Organization of the United Nations. 29 classes in the registry index, 27 in the legend file, 26 matched by code or name.

Reference: The Islamic Republic of Afghanistan, Land cover atlas. (2016), http://www.fao.org/geospatial/resources/detail/en/c/1024570/

## Datasets (1)

- Aggregated Land Cover Database of the Islamic Republic of Afghanistan (2010) (iso/1dd35e22-bd51-4c4d-bf0c-546baababe74)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| 1A | [Settlements/urban areas](classes/1A.md) | This class includes urban areas with gardens. |
| 1B | [Non urban builtup areas](classes/1B.md) | This class includes airports, industrial areas and vegetated areas within large non-urban zones. it also incl… |
| 2A | [Fruit trees](classes/2A.md) | Tree crops (Orchads) with surface irrigation. |
| 2B | [Vineyard](classes/2B.md) | Vineyards with surface irrigation. |
| 3A(1) | [Intesively cultivated area (component 1 of mixed class)](classes/3A-1.md) | This class is the component 1 of mixed class (intensively irrigated area). |
| 3A(2) | [Intesively irrigated area (component 2 of mixed class)](classes/3A-2.md) | This class is the component 2 of mixed class (intensively irrigated area). |
| 3A | [Intensely irrigated area](classes/3A.md) | Irrigated herbaceous crops inside a very intensively cultivated area. The environmental conditions where this… |
| 3A1(1) | [Irrigated crop (component 1 of mixed class)](classes/3A1-1.md) | This class is the component 1 of mixed class (irrigated herbaceous crops). |
| 3A1(2) | [Irrigated crop (component 2 of mixed class)](classes/3A1-2.md) | This class is the component 2 of mixed class (irrigated herbaceous crops). |
| 3A1 | [Irrigated herbaceous crop](classes/3A1.md) | This class can be found in most regions, including dry areas and where the surface water supply is not persis… |
| 3B | [Marginal irrigated crops](classes/3B.md) | Agricultural lands in a marginal agricultural area, usually devoid of active fields. It also represents the n… |
| 3C | [Karez system](classes/3C.md) | Herbaceous crops with surface irrigation derived from an active karez system. Only the active fields, detecte… |
| 4A | [Rainfed cultivation in flat areas](classes/4A.md) | Rainfed cultivation of herbaceous crops (graminoids) in flat (to almost flat) regions. |
| 4B | [Rainfed cultivation in sloping land](classes/4B.md) | Rainfed cultivation of herbaceous crops (graminoids) in sloping/rolling regions. |
| 6A | [Closed trees](classes/6A.md) | Closed (>65 %) needle leaved evergreen trees. |
| 6B | [Open trees](classes/6B.md) | Open (65-15 %) needle leaved evergreen trees. |
| 6B1 | [Open trees undifferentiated](classes/6B1.md) | Undifferentiated trees/woodland with open (65-15%) cover. |
| 6C | [Close to open shrubland](classes/6C.md) | Shrubland composed of closed to open (100-15 %) shrubs. |
| 7 | [Rangeland](classes/7.md) | Natural sparse (15-1 %) dwarf shrubs or open (65-15 %) short Herbaceous vegetation or sparse (15-1 %) short h… |
| 8A | [Bare soil or rock outcrops](classes/8A.md) | Bare soil or rock outcrops. |
| 8B | [Sandy areas](classes/8B.md) | Loose and shifting sands. This class may be mixed with natural vegetation for very short periods in the rainy… |
| 8C | [Dunes](classes/8C.md) | Sand dunes. This class may be mixed with natural vegetation for very short periods in the rainy season. |
| 9A | [Marsh (permanently innundated)](classes/9A.md) | Closed to open (100-45 %) natural herbaceous vegetation on a permanently flooded area. |
| 9B | [Seasonally innundated vegetation](classes/9B.md) | Closed to Open (100-15 %) natural Herbaceous vegetation on a temporarily flooded area or closed to open (100-… |
| 10A | [Artifiicial and natural waterbodies](classes/10A.md) | Perennial standing fresh water bodies, either natural or artificial. |
| 10B | [Seasonal lakes](classes/10B.md) | Non perennial standing water bodies with duration of water presence less than 4 months. Bare soil surfaces ar… |
| 11 | [River](classes/11.md) | Perennial rivers. Fresh water flowing more than 9 months/year. |
| 12 | [River banks](classes/12.md) | This class describes both the area of maximum expansion of a perennial river and the beds of seasonal streams. |
| 13 | [Perenial snow](classes/13.md) | Perennial snow (more than 9 months/year) and glaciers. |
