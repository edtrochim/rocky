---
id: registry:L48
kind: system
title: Land cover legend for Gaza
alpha_code: L48
country: State of Palestine
m49: 275
iso3: PSE
year: 2024
status: valid
legend_type: LCCS3
format: lccs3
publisher: Food and Agriculture Organization of the United Nations
reference_link: https://openknowledge.fao.org/handle/20.500.14283/cb7167en
reference_file: Ref_48.pdf
n_classes_index: 7
n_classes_file: 7
n_classes_matched: 7
n_datasets: 1
files:
- okf/registry/_raw/L48/L48.csv
- okf/registry/_raw/L48/L48.lccs
- okf/registry/_raw/L48/L48.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L48:IC
  path: classes/IC.md
- rel: has_class
  id: registry:L48:RC
  path: classes/RC.md
- rel: has_class
  id: registry:L48:O
  path: classes/O.md
- rel: has_class
  id: registry:L48:Gh
  path: classes/Gh.md
- rel: has_class
  id: registry:L48:Bl
  path: classes/Bl.md
- rel: has_class
  id: registry:L48:Bu
  path: classes/Bu.md
- rel: has_class
  id: registry:L48:Wb
  path: classes/Wb.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# Land cover legend for Gaza

State of Palestine · 2024 · LCCS3 · status valid. Publisher: Food and Agriculture Organization of the United Nations. 7 classes in the registry index, 7 in the legend file, 7 matched by code or name.

Reference: Report for Impact of the May conflict escalation on the agricultural area in the Gaza Strip (2021) (2021), https://openknowledge.fao.org/handle/20.500.14283/cb7167en

## Datasets (1)

- Land Cover (Gaza, Palestine - 2021 - 5m) (iso/0597b3b5-4698-49e7-aa1b-ba735bba6836)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| IC | [Irrigated crops](classes/IC.md) | Cropland where the water source comes from irrigation. Most of the crops planted are vegetables. The most com… |
| RC | [Rainfed crops](classes/RC.md) | Cropland where the water source depends on the rainwater. Most of the crops planted are herbaceous main crops… |
| O | [Orchards or home garden](classes/O.md) | Cropland that are covered by shrubs or trees crops which can be either mixed or single type. The crops cover … |
| Gh | [Greenhouse](classes/Gh.md) | A structure built in order to regulate the climate/environment; therefore, the plants inside can thrive. Huma… |
| Bl | [Bare land (current fallow)](classes/Bl.md) | Land cover which consists of bare soils either natural or cropland that through fallow period (cultivation ab… |
| Bu | [Built-up](classes/Bu.md) | This class includes artificial surfaces, both non-linear and linear built-up areas including roadways, indust… |
| Wb | [Water body](classes/Wb.md) | Water bodies that include both natural and artificial waterbodies. The class includes rivers, ponds, and lake… |
