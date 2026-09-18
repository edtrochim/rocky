---
id: registry:L51
kind: system
title: National land cover legend for Syria
alpha_code: L51
country: Syrian Arab Republic
m49: 760
iso3: SYR
year: 2025
status: valid
legend_type: LCHS
format: lchs
publisher: ''
reference_link: ''
reference_file: ''
n_classes_index: 10
n_classes_file: 10
n_classes_matched: 10
n_datasets: 1
files:
- okf/registry/_raw/L51/L51.csv
- okf/registry/_raw/L51/L51.LChS
- okf/registry/_raw/L51/L51.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L51:Cf
  path: classes/Cf.md
- rel: has_class
  id: registry:L51:Of
  path: classes/Of.md
- rel: has_class
  id: registry:L51:Sh
  path: classes/Sh.md
- rel: has_class
  id: registry:L51:Gl
  path: classes/Gl.md
- rel: has_class
  id: registry:L51:Or
  path: classes/Or.md
- rel: has_class
  id: registry:L51:Rc
  path: classes/Rc.md
- rel: has_class
  id: registry:L51:Ic
  path: classes/Ic.md
- rel: has_class
  id: registry:L51:Ba
  path: classes/Ba.md
- rel: has_class
  id: registry:L51:Bu
  path: classes/Bu.md
- rel: has_class
  id: registry:L51:Wa
  path: classes/Wa.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# National land cover legend for Syria

Syrian Arab Republic · 2025 · LCHS · status valid. Publisher: not stated. 10 classes in the registry index, 10 in the legend file, 10 matched by code or name.

## Datasets (1)

- National land cover map for Syria (iso/a4225e44-f542-426e-add3-d3e5ff233800)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| Cf | [Closed forest​](classes/Cf.md) | Land area with tree cover from 70 to 100 %. Undifferentiated trees, sometimes mixed broadleaved and needle-le… |
| Of | [Open ​forest](classes/Of.md) | Land area with tree cover from 20 to 70%. Undifferentiated trees, sometimes mixed broadleaved and needle-leav… |
| Sh | [Shrublands​](classes/Sh.md) | Land area with shrub cover >10%. The shrub foliage can be either evergreen or deciduous.​ |
| Gl | [Grasslands​](classes/Gl.md) | Land area with herbaceous types of cover (>10%). Tree cover < 10%. Shrub cover < 10%​ |
| Or | [Orchards​](classes/Or.md) | Cultivated agriculture with rainfed area where the growth form tree is dominant.​ |
| Rc | [Rainfed croplands​](classes/Rc.md) | Land area covered with temporary rainfed herbaceous crops followed by harvest and a bare soil period.​ |
| Ic | [Irrigated croplands​](classes/Ic.md) | Cultivated agriculture where herbaceous crops are predominantly grown under permanent or seasonal irrigation,… |
| Ba | [Barren​](classes/Ba.md) | Areas dominated by bare soil, rock, or unconsolidated material, which maintain very sparse vegetation cover (… |
| Bu | [Built-up​](classes/Bu.md) | Areas dominated by artificial structures such as buildings, roads and other paved or compacted surfaces, wher… |
| Wa | [Water​](classes/Wa.md) | Permanent or seasonally flooded surfaces covered by inland or coastal water bodies (e.g. rivers, lakes, reser… |
