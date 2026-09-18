---
id: registry:L39
kind: system
title: Worldcover 2020 legend
alpha_code: L39
country: Global
m49: 1
iso3: ' - '
year: 2020
status: pending
legend_type: LCCS3
format: lccs3
publisher: European Space Agency
reference_link: https://worldcover2020.esa.int/data/docs/WorldCover_PUM_V1.1.pdf
reference_file: Ref_39.pdf
n_classes_index: 11
n_classes_file: 11
n_classes_matched: 11
n_datasets: 1
files:
- okf/registry/_raw/L39/L39.csv
- okf/registry/_raw/L39/L39.lccs
- okf/registry/_raw/L39/L39.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L39:10
  path: classes/10.md
- rel: has_class
  id: registry:L39:20
  path: classes/20.md
- rel: has_class
  id: registry:L39:30
  path: classes/30.md
- rel: has_class
  id: registry:L39:40
  path: classes/40.md
- rel: has_class
  id: registry:L39:50
  path: classes/50.md
- rel: has_class
  id: registry:L39:60
  path: classes/60.md
- rel: has_class
  id: registry:L39:70
  path: classes/70.md
- rel: has_class
  id: registry:L39:80
  path: classes/80.md
- rel: has_class
  id: registry:L39:90
  path: classes/90.md
- rel: has_class
  id: registry:L39:95
  path: classes/95.md
- rel: has_class
  id: registry:L39:100
  path: classes/100.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# Worldcover 2020 legend

Global · 2020 · LCCS3 · status pending. Publisher: European Space Agency. 11 classes in the registry index, 11 in the legend file, 11 matched by code or name.

Reference: World Cover - Product User Manual (2020), https://worldcover2020.esa.int/data/docs/WorldCover_PUM_V1.1.pdf

## Datasets (1)

- Worldcover 2020 (no GeoNetwork id)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| 10 | [Tree Cover](classes/10.md) | This class includes any geographic area dominated by trees with a cover of 10% or more. Other land cover clas… |
| 20 | [Shrubland](classes/20.md) | This class includes any geographic area dominated by natural shrubs having a cover of 10% or more. Shrubs are… |
| 30 | [Grassland](classes/30.md) | This class includes any geographic area dominated by natural herbaceous plants (Plants without persistent ste… |
| 40 | [Cropland](classes/40.md) | Land covered with annual cropland that is sowed/planted and harvestable at least once within the 12 months af… |
| 50 | [Built-up](classes/50.md) | Land covered by buildings, roads and other man-made structures such as railroads. Buildings include both resi… |
| 60 | [Bare / sparse vegetation](classes/60.md) | Lands with exposed soil, sand, or rocks and never has more than 10 % vegetated cover during any time of the y… |
| 70 | [Snow and Ice](classes/70.md) | This class includes any geographic area covered by snow or glaciers persistently |
| 80 | [Permanent water bodies](classes/80.md) | This class includes any geographic area covered for most of the year (more than 9 months) by water bodies: la… |
| 90 | [Herbaceous wetland](classes/90.md) | Land dominated by natural herbaceous vegetation (cover of 10% or more) that is permanently or regularly flood… |
| 95 | [Mangroves](classes/95.md) | Taxonomically diverse, salt-tolerant tree and other plant species which thrive in intertidal zones of shelter… |
| 100 | [Moss and lichen](classes/100.md) | Land covered with lichens and/or mosses. Lichens are composite organisms formed from the symbiotic associatio… |
