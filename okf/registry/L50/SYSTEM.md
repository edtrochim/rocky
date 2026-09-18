---
id: registry:L50
kind: system
title: Land cover legend for Libya
alpha_code: L50
country: Libya
m49: 434
iso3: LBY
year: 2025
status: valid
legend_type: LCHS
format: lchs
publisher: Food and Agriculture Organization of the United Nations
reference_link: https://openknowledge.fao.org/items/8701b6b7-5c35-497b-a251-8ebe7ab96e13
reference_file: Ref_50.pdf
n_classes_index: 12
n_classes_file: 0
n_classes_matched: 0
n_datasets: 1
files:
- okf/registry/_raw/L50/L50.csv
- okf/registry/_raw/L50/L50.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L50:Fo
  path: classes/Fo.md
- rel: has_class
  id: registry:L50:Sh
  path: classes/Sh.md
- rel: has_class
  id: registry:L50:Gr
  path: classes/Gr.md
- rel: has_class
  id: registry:L50:Cr
  path: classes/Cr.md
- rel: has_class
  id: registry:L50:Ci
  path: classes/Ci.md
- rel: has_class
  id: registry:L50:Or
  path: classes/Or.md
- rel: has_class
  id: registry:L50:Bs
  path: classes/Bs.md
- rel: has_class
  id: registry:L50:Ro
  path: classes/Ro.md
- rel: has_class
  id: registry:L50:Bu
  path: classes/Bu.md
- rel: has_class
  id: registry:L50:Aw
  path: classes/Aw.md
- rel: has_class
  id: registry:L50:Sw
  path: classes/Sw.md
- rel: has_class
  id: registry:L50:Se
  path: classes/Se.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# Land cover legend for Libya

Libya · 2025 · LCHS · status valid. Publisher: Food and Agriculture Organization of the United Nations. 12 classes in the registry index, 0 in the legend file, 0 matched by code or name.

Reference: Historical assessment of agricultural drought impact in the Syrian Arab Republic (2021–2025) (2026), https://openknowledge.fao.org/items/8701b6b7-5c35-497b-a251-8ebe7ab96e13

## Datasets (1)

- Land Cover (Libya - 10m - 2025 - 12 classes) (iso/2c2d1b46-1337-4eb7-9033-95d06d0afdec)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| Fo | [Forest](classes/Fo.md) | It corresponds to areas with natural semi-natural vegetation where the growth form tree is dominant. |
| Sh | [Shrubland](classes/Sh.md) | It corresponds to areas with natural semi-natural vegetation where the growth form shrub is dominant. |
| Gr | [Grassland](classes/Gr.md) | This level corresponds to an area of natural vegetation with the mandatory presence of herbs. |
| Cr | [Cultivated rainfed](classes/Cr.md) | Agricultural land where crops rely mainly on rainfall, without permanent irrigation infrastructure. |
| Ci | [Cultivated irrigated](classes/Ci.md) | Agricultural land supplied with water through irrigation systems (pivots, wells...), enabling cultivation ind… |
| Or | [Orchards](classes/Or.md) | Cultivated areas planted with perennial tree crops (dates, olives, fruit trees), arranged in regular patterns… |
| Bs | [Bare Soil / Sand](classes/Bs.md) | Areas with little or no vegetation cover, including deserts, dunes, and exposed soils. |
| Ro | [Rocks](classes/Ro.md) | Exposed rocky surfaces with minimal or no soil and vegetation cover. |
| Bu | [Built up](classes/Bu.md) | Areas dominated by buildings and infrastructure, including residential, industrial, and transportation surfac… |
| Aw | [Artificial water](classes/Aw.md) | Permanent or semi-permanent water bodies created by human activity, such as reservoirs, dams, irrigation basi… |
| Sw | [Seasonal water](classes/Sw.md) | Natural or artificial water bodies that appear temporarily after rainfall or flooding and dry out part of the… |
| Se | [Sebkha](classes/Se.md) | Saline depressions that are episodically flooded and often dry, typically covered by salt crusts and lacking … |
