---
id: registry:L43
kind: system
title: National land cover legend for Libya
alpha_code: L43
country: Libya
m49: 434
iso3: LBY
year: 2022
status: superceeded
legend_type: LCCS3
format: lccs3
publisher: Food and Agriculture Organization of the United Nations
reference_link: https://openknowledge.fao.org/items/1680d3e5-ae46-410a-afd9-5b01f3377e1c
reference_file: Ref_43.pdf
n_classes_index: 9
n_classes_file: 9
n_classes_matched: 9
n_datasets: 1
files:
- okf/registry/_raw/L43/L43.csv
- okf/registry/_raw/L43/L43.lccs
- okf/registry/_raw/L43/L43.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L43:Tt
  path: classes/Tt.md
- rel: has_class
  id: registry:L43:St
  path: classes/St.md
- rel: has_class
  id: registry:L43:GL
  path: classes/GL.md
- rel: has_class
  id: registry:L43:War
  path: classes/War.md
- rel: has_class
  id: registry:L43:Cr
  path: classes/Cr.md
- rel: has_class
  id: registry:L43:Ci
  path: classes/Ci.md
- rel: has_class
  id: registry:L43:Ast
  path: classes/Ast.md
- rel: has_class
  id: registry:L43:Nst
  path: classes/Nst.md
- rel: has_class
  id: registry:L43:W
  path: classes/W.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# National land cover legend for Libya

Libya · 2022 · LCCS3 · status superceeded. Publisher: Food and Agriculture Organization of the United Nations. 9 classes in the registry index, 9 in the legend file, 9 matched by code or name.

Reference: Integrated methodological framework and assessment of water management infrastructure, crop and water productivity in Libya (2025), https://openknowledge.fao.org/items/1680d3e5-ae46-410a-afd9-5b01f3377e1c

## Datasets (1)

- Land Cover (Libya - 10 m - 2022 - 9 classes) (iso/2d3fb746-3691-4b97-b596-01c5ae636350)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| Tt | [Tree-dominated area (terrestiral)](classes/Tt.md) | It corresponds to areas with natural semi-natural vegetation where the growth form tree is dominant. |
| St | [Shrub-dominated area](classes/St.md) | It corresponds to areas with natural semi-natural vegetation where the growth form shrub is dominant. |
| GL | [Grassland](classes/GL.md) | This level corresponds to an area of natural vegetation with the mandatory presence of herbs. |
| War | [Mangroves (woody dominated aquatic areas)](classes/War.md) | Areas dominated by Mangroves i.e. coastal salt tolerant species. |
| Cr | [Cultivated rainfed area](classes/Cr.md) | Agricultural land where crops rely mainly on rainfall, without permanent irrigation infrastructure. |
| Ci | [Cultivated irrigated area](classes/Ci.md) | Agricultural land supplied with water through irrigation systems (pivots, wells...), enabling cultivation ind… |
| Ast | [Artificial surfaces](classes/Ast.md) | Areas dominated by buildings and infrastructure, including residential, industrial, and transportation surfac… |
| Nst | [Natural surfaces](classes/Nst.md) | Areas dominated by soil, sand and rock surfaces. |
| W | [Water](classes/W.md) | Area covered by natural or artificial water bodies. |
