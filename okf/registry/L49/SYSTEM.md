---
id: registry:L49
kind: system
title: Land cover legend for Nigeria (2025)
alpha_code: L49
country: Nigeria
m49: 566
iso3: NGA
year: 2025
status: valid
legend_type: LCHS
format: lchs
publisher: ''
reference_link: ''
reference_file: ''
n_classes_index: 12
n_classes_file: 12
n_classes_matched: 12
n_datasets: 0
files:
- okf/registry/_raw/L49/L49.csv
- okf/registry/_raw/L49/L49.LChS
- okf/registry/_raw/L49/L49.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L49:Ad
  path: classes/Ad.md
- rel: has_class
  id: registry:L49:Ac
  path: classes/Ac.md
- rel: has_class
  id: registry:L49:Ab
  path: classes/Ab.md
- rel: has_class
  id: registry:L49:Sv
  path: classes/Sv.md
- rel: has_class
  id: registry:L49:GL
  path: classes/GL.md
- rel: has_class
  id: registry:L49:Vnar
  path: classes/Vnar.md
- rel: has_class
  id: registry:L49:Fsw
  path: classes/Fsw.md
- rel: has_class
  id: registry:L49:Can
  path: classes/Can.md
- rel: has_class
  id: registry:L49:Ca
  path: classes/Ca.md
- rel: has_class
  id: registry:L49:Sa
  path: classes/Sa.md
- rel: has_class
  id: registry:L49:Sn
  path: classes/Sn.md
- rel: has_class
  id: registry:L49:E
  path: classes/E.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# Land cover legend for Nigeria (2025)

Nigeria · 2025 · LCHS · status valid. Publisher: not stated. 12 classes in the registry index, 12 in the legend file, 12 matched by code or name.

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| Ad | [Closed forest](classes/Ad.md) | This land cover is characterized by the presence of evergreen plants of high species diversity; the canopy ca… |
| Ac | [Open forest](classes/Ac.md) | This land cover class is characterized by the presence of one mandatory tree stratum that defines the overall… |
| Ab | [Shrubland](classes/Ab.md) | This land cover class is characterized by the presence of one mandatory stratum of shrubs. The species are in… |
| Sv | [Savanna woodland](classes/Sv.md) | This land cover class is characterized by the presence of two strata, which include grasslands with scattered… |
| GL | [Savanna grassland](classes/GL.md) | This land cover class is characterized by the presence of herbaceous growth form and woody growth forms It is… |
| Vnar | [Mangroves](classes/Vnar.md) | This land cover class is characterized by marine vegetation found in close proximity to the ocean, creeks and… |
| Fsw | [Freshwater swamps](classes/Fsw.md) | This land cover class is characterized by all vegetation along freshwater, riverbanks and marshy areas. The c… |
| Can | [Annual crops](classes/Can.md) | This land cover class is characterized by the plants that complete their life cycle from planting to harvesti… |
| Ca | [Permanent crops](classes/Ca.md) | This land cover class is characterized by polygons with regular boundaries similar to crop land but usually h… |
| Sa | [Artificial surfaces](classes/Sa.md) | This land cover class is characterized by the presence of built-up areas. Usually, the original natural cover… |
| Sn | [Bare surfaces](classes/Sn.md) | This class represents land surfaces with little to no plant cover. These areas may be characterized by aeolia… |
| E | [Water](classes/E.md) | This class represents all types of water including, streams, rivers, lakes, ponds, reservoirs and oceans. (FA… |
