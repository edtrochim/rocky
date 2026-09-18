---
id: registry:L41
kind: system
title: National land cover legend for Ukraine
alpha_code: L41
country: Ukraine
m49: 804
iso3: UKR
year: 2024
status: valid
legend_type: LCCS3
format: lccs3
publisher: Food and Agriculture Organization of the United Nations
reference_link: Pending
reference_file: Pending
n_classes_index: 15
n_classes_file: 15
n_classes_matched: 15
n_datasets: 1
files:
- okf/registry/_raw/L41/L41.csv
- okf/registry/_raw/L41/L41.lccs
- okf/registry/_raw/L41/L41.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L41:Ct
  path: classes/Ct.md
- rel: has_class
  id: registry:L41:Ot
  path: classes/Ot.md
- rel: has_class
  id: registry:L41:Vst
  path: classes/Vst.md
- rel: has_class
  id: registry:L41:Cs
  path: classes/Cs.md
- rel: has_class
  id: registry:L41:Os
  path: classes/Os.md
- rel: has_class
  id: registry:L41:Vss
  path: classes/Vss.md
- rel: has_class
  id: registry:L41:H
  path: classes/H.md
- rel: has_class
  id: registry:L41:Hn
  path: classes/Hn.md
- rel: has_class
  id: registry:L41:Rmo
  path: classes/Rmo.md
- rel: has_class
  id: registry:L41:Rhc
  path: classes/Rhc.md
- rel: has_class
  id: registry:L41:Ihc
  path: classes/Ihc.md
- rel: has_class
  id: registry:L41:Bs
  path: classes/Bs.md
- rel: has_class
  id: registry:L41:As
  path: classes/As.md
- rel: has_class
  id: registry:L41:Pw
  path: classes/Pw.md
- rel: has_class
  id: registry:L41:Sw
  path: classes/Sw.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# National land cover legend for Ukraine

Ukraine · 2024 · LCCS3 · status valid. Publisher: Food and Agriculture Organization of the United Nations. 15 classes in the registry index, 15 in the legend file, 15 matched by code or name.

Reference: National land cover map for Ukraine (2024), Pending

## Datasets (1)

- National land cover map for Ukraine (no GeoNetwork id)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| Ct | [Closed Tree Dominated](classes/Ct.md) | Areas with closed (>80%) tree canopy cover. Trees are predominantly broadleaved or mixed (broadleaved and nee… |
| Ot | [Open Tree Dominated](classes/Ot.md) | Open tree cover (20-80%), commonly found in parkland or transitional areas. Trees are often a mix of broadlea… |
| Vst | [Very Open/Sparse Tree Dominated](classes/Vst.md) | Sparse tree cover (4-20%), often located in transitional zones between forests and open landscapes, or in deg… |
| Cs | [Closed Shrub Dominated](classes/Cs.md) | Dense (>80%) shrub cover. Shrubs can be either evergreen or deciduous, often found in forest-steppe or dry ar… |
| Os | [Open Shrub Dominated](classes/Os.md) | Shrub cover (20-80%), typically in transitional zones, degraded lands, or dry steppe regions. |
| Vss | [Very Open/Sparse Shrub Dominated](classes/Vss.md) | Sparse shrub cover (4-20%), found in degraded shrublands or steppe-forest transition zones. |
| H | [Herbs Dominated](classes/H.md) | Areas dominated by herbaceous plants (>20% cover), commonly found in meadows, pastures, or steppe ecosystems. |
| Hn | [Aquatic Herbs dominated areas](classes/Hn.md) | Wetlands or floodplains with dominant herbaceous vegetation, such as reeds, sedges, or other hydrophilic plan… |
| Rmo | [Orchards](classes/Rmo.md) | Cultivated agricultural areas with fruit-bearing trees typically in rainfed systems. |
| Rhc | [Herbaceous Crops rainfed](classes/Rhc.md) | Areas covered with rainfed herbaceous growth forms, such as maize, wheat, barley, and sunflowers. These field… |
| Ihc | [Herbaceous Crops Irrigated](classes/Ihc.md) | It corresponds to areas with cultivated irrigated agriculture where the growth form herb is dominant. These a… |
| Bs | [Bare soil](classes/Bs.md) | Exposed soil areas with no vegetation (<4%), often due to erosion or overuse of agricultural lands. Exposed r… |
| As | [Articial Surface](classes/As.md) | Built-up areas with residential, commercial, or industrial structures and related infrastructure. All artfici… |
| Pw | [Permanent water](classes/Pw.md) | Natural or artificial water bodies (e.g., lakes, reservoirs) with continuous water presence throughout the ye… |
| Sw | [Seasonal water](classes/Sw.md) | Water bodies or wetlands with intermittent water presence, typically seasonal (e.g., spring flooding). |
