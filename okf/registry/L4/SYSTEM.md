---
id: registry:L4
kind: system
title: National land cover legend for Nigeria
alpha_code: L4
country: Nigeria
m49: 566
iso3: NGA
year: 2020
status: valid
legend_type: LCCS3
format: lccs3
publisher: The Food and Agriculture Organization of United Nations
reference_link: https://www.fao.org/3/cb1327en/cb1327en.pdf
reference_file: Ref_4.pdf
n_classes_index: 12
n_classes_file: 12
n_classes_matched: 12
n_datasets: 1
files:
- okf/registry/_raw/L4/L4.csv
- okf/registry/_raw/L4/L4.eapx
- okf/registry/_raw/L4/L4.lccs
- okf/registry/_raw/L4/L4.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L4:UF
  path: classes/UF.md
- rel: has_class
  id: registry:L4:DF
  path: classes/DF.md
- rel: has_class
  id: registry:L4:FSW
  path: classes/FSW.md
- rel: has_class
  id: registry:L4:MF
  path: classes/MF.md
- rel: has_class
  id: registry:L4:FP
  path: classes/FP.md
- rel: has_class
  id: registry:L4:AL
  path: classes/AL.md
- rel: has_class
  id: registry:L4:SV
  path: classes/SV.md
- rel: has_class
  id: registry:L4:GL
  path: classes/GL.md
- rel: has_class
  id: registry:L4:TP
  path: classes/TP.md
- rel: has_class
  id: registry:L4:BS
  path: classes/BS.md
- rel: has_class
  id: registry:L4:ST
  path: classes/ST.md
- rel: has_class
  id: registry:L4:WB
  path: classes/WB.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# National land cover legend for Nigeria

Nigeria · 2020 · LCCS3 · status valid. Publisher: The Food and Agriculture Organization of United Nations. 12 classes in the registry index, 12 in the legend file, 12 matched by code or name.

Reference: Land use/Land Cover and Forest Cover Mapping in Nigeria (2020), https://www.fao.org/3/cb1327en/cb1327en.pdf

## Datasets (1)

- Land use/Land Cover and Forest Cover Mapping in Nigeria (No)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| UF | [Undisturbed forest](classes/UF.md) | Natural or seminatural trees, shrubs and herbaceous growth forms. |
| DF | [Disturbed forst](classes/DF.md) | Natural or seminatural trees, shrubs and herbaceous growth forms which has been degraded by cultural activite… |
| FSW | [Freshwater swamp forest](classes/FSW.md) | Freshwater swamp land dominated by trees. |
| MF | [Mangrove forest](classes/MF.md) | Saltwater mangrove forest |
| FP | [Forest plantation](classes/FP.md) | Cultivated and managed forest plantation. |
| AL | [Arable land](classes/AL.md) | Cultivated and managed land dominated by herbaceous growth forms. |
| SV | [Savanna woodland](classes/SV.md) | Natural grassland with scattered woody growth vegetation. |
| GL | [Grassland](classes/GL.md) | Grassland dominated by herbaous growth forms. |
| TP | [Tree crop plantation](classes/TP.md) | Cultivated and managed cocoa and palm plantations. |
| BS | [Bare surfaces](classes/BS.md) | Bare surfaces dominated by bare soil and non-built up areas. |
| ST | [Settlements](classes/ST.md) | Built-up areas. |
| WB | [Water bodies](classes/WB.md) | Water bodies. |
