---
id: registry:L36
kind: system
title: National land cover legend for Tunisia
alpha_code: L36
country: Tunisia
m49: 788
iso3: TUN
year: 2024
status: valid
legend_type: LCCS3
format: lccs3
publisher: Food and Agriculture Organization of the United Nations
reference_link: https://openknowledge.fao.org/items/76671622-88fe-4daa-8493-b5d4a8d517e2
reference_file: Ref_36.pdf
n_classes_index: 12
n_classes_file: 12
n_classes_matched: 11
n_datasets: 1
files:
- okf/registry/_raw/L36/L36.lccs
- okf/registry/_raw/L36/L36.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L36:Fp
  path: classes/Fp.md
- rel: has_class
  id: registry:L36:Fi
  path: classes/Fi.md
- rel: has_class
  id: registry:L36:ZNV
  path: classes/ZNV.md
- rel: has_class
  id: registry:L36:A
  path: classes/A.md
- rel: has_class
  id: registry:L36:SA
  path: classes/SA.md
- rel: has_class
  id: registry:L36:Abr
  path: classes/Abr.md
- rel: has_class
  id: registry:L36:Op
  path: classes/Op.md
- rel: has_class
  id: registry:L36:Oi
  path: classes/Oi.md
- rel: has_class
  id: registry:L36:Cp
  path: classes/Cp.md
- rel: has_class
  id: registry:L36:Ci
  path: classes/Ci.md
- rel: has_class
  id: registry:L36:Oai
  path: classes/Oai.md
- rel: has_class
  id: registry:L36:EZH
  path: classes/EZH.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# National land cover legend for Tunisia

Tunisia · 2024 · LCCS3 · status valid. Publisher: Food and Agriculture Organization of the United Nations. 12 classes in the registry index, 12 in the legend file, 11 matched by code or name.

Reference: Mapping land cover in Tunisia (2024), https://openknowledge.fao.org/items/76671622-88fe-4daa-8493-b5d4a8d517e2

## Datasets (1)

- National land cover map for Tunisia (iso/5eb4eab6-47b2-477b-84e9-2d04bc0b88a3)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| Fp | [Rainfed orchards](classes/Fp.md) | The land is covered by rainfed orchards cultivated for the production of fruits (i.e., orange, citrus, fig, a… |
| Fi | [Irrigated orchards](classes/Fi.md) | The land is covered by irrigated orchards cultivated for the production of fruits (i.e., orange, citrus, fig,… |
| ZNV | [Bare soIl](classes/ZNV.md) | The land is covered by bare area/undifferentiated area not used for cultivation and usuallydevoid of grass an… |
| A | [Forest](classes/A.md) | The land is primarily covered by desnse natural forests with the presence of bushes and shrubs also possible. |
| SA | [Infrastructure](classes/SA.md) | The land is covered by infrastructure as buildings, roads and artifiical surfaced areas. Different types of b… |
| Abr | [Marquis/garrigue](classes/Abr.md) | The land is covered by relatively dense shrubs, ocassionally interspersed with sparse trees and herbaceous ve… |
| Op | [Rainfed olives](classes/Op.md) | The land is covered by rainfed olive orchards. These cultivated groves are characterized by the sparse cluste… |
| Oi | [Irrigated olives](classes/Oi.md) | The land is covered by irrigated olive orchards. These cultivated groves are characterized by the sparse clus… |
| Cp | [Other rainfed crop](classes/Cp.md) | The land is covered by rainfed agricultural fields, featuring various types of crops: cereal crops such as wh… |
| Ci | [Other irrigated crop](classes/Ci.md) | The land is covered by irrigated agricultural fields, featuring various types of crops: cereal crops such as … |
| Oai | [Irrigated dates](classes/Oai.md) | The land is covered by irrigated date. The presence of date tress dominates the land cover (about 80 %). In s… |
| EZH | [Water and wetlands](classes/EZH.md) | The land is covered by water areas. Within this land cover class are included natural and artificial non - pe… |
