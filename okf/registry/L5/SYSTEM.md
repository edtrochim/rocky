---
id: registry:L5
kind: system
title: Land cover legend for Punjab Province, Pakistan
alpha_code: L5
country: Pakistan
m49: 586
iso3: PAK
year: 2020
status: valid
legend_type: LCCS3
format: lccs3
publisher: Food and Agriculture Organization of the United Nations
reference_link: '-'
reference_file: Ref_5.pdf
n_classes_index: 18
n_classes_file: 18
n_classes_matched: 18
n_datasets: 1
files:
- okf/registry/_raw/L5/L5.csv
- okf/registry/_raw/L5/L5.eapx
- okf/registry/_raw/L5/L5.lccs
- okf/registry/_raw/L5/L5.xsd
vocabulary:
  errors: 1
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L5:BUP
  path: classes/BUP.md
- rel: has_class
  id: registry:L5:ROA
  path: classes/ROA.md
- rel: has_class
  id: registry:L5:ORC
  path: classes/ORC.md
- rel: has_class
  id: registry:L5:HCI
  path: classes/HCI.md
- rel: has_class
  id: registry:L5:HCR
  path: classes/HCR.md
- rel: has_class
  id: registry:L5:HCF
  path: classes/HCF.md
- rel: has_class
  id: registry:L5:HER
  path: classes/HER.md
- rel: has_class
  id: registry:L5:SOP
  path: classes/SOP.md
- rel: has_class
  id: registry:L5:SCL
  path: classes/SCL.md
- rel: has_class
  id: registry:L5:SWE
  path: classes/SWE.md
- rel: has_class
  id: registry:L5:TOP
  path: classes/TOP.md
- rel: has_class
  id: registry:L5:TFP
  path: classes/TFP.md
- rel: has_class
  id: registry:L5:TCL
  path: classes/TCL.md
- rel: has_class
  id: registry:L5:SDU
  path: classes/SDU.md
- rel: has_class
  id: registry:L5:BSO
  path: classes/BSO.md
- rel: has_class
  id: registry:L5:BTW
  path: classes/BTW.md
- rel: has_class
  id: registry:L5:WBO
  path: classes/WBO.md
- rel: has_class
  id: registry:L5:WET
  path: classes/WET.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# Land cover legend for Punjab Province, Pakistan

Pakistan · 2020 · LCCS3 · status valid. Publisher: Food and Agriculture Organization of the United Nations. 18 classes in the registry index, 18 in the legend file, 18 matched by code or name.

Reference: Land cover mapping for Punjab province, Pakistan (2020), -

## Datasets (1)

- Land Cover of Punjab Province - Pakistan (iso/4f8d2bd2-9f7a-423c-97f0-55071ba48bf3)

## Vocabulary check of the registry file

1 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| BUP | [Built-up](classes/BUP.md) | The land covered by buildings, roads and artificial surfaced ar-eas. Different types of build-up are included… |
| ROA | [Roads](classes/ROA.md) | Linear artificial structures, mainly major roads (motor-ways, primary roads). |
| ORC | [Tree orchards](classes/ORC.md) | Orchards are areas cultivated for the production of fruits, nuts, and other type of plantations. Areas covere… |
| HCI | [Herbaceous crops irrigated](classes/HCI.md) | Agricultural areas characterized by ex-tensive irrigational facilities. The pres-ence channels for irrigation… |
| HCR | [Herbaceous crops rainfed](classes/HCR.md) | Rainfed agricul-ture relies only on rainfall for wa-ter, therefore NDVI values strictly depend on rainfall pa… |
| HCF | [Herbaceous crops in flood plain](classes/HCF.md) | Herbaceous crop located only in proximity of the riverbed is termed as crop in floodplain. The water supply i… |
| HER | [Herbaceous natural vegetation](classes/HER.md) | Relatively dense herba-ceous natural vegetation, occasionally with sparse shrubs and trees. NDVI values are v… |
| SOP | [Shrubs sparse natural vegetation](classes/SOP.md) | Natural open shrubs, occasionally with sparse or closed herba-ceous vegetation cov-er, with percentage cover … |
| SCL | [Shrubs dense natural vegetation](classes/SCL.md) | Natural closed shrubs with shrubs percentage cover of more than 60%. In Punjab the forest cover is limited, a… |
| SWE | [Shrubs in temporary wet soil](classes/SWE.md) | This class includes areas mainly covered by shrubs of-ten with herbaceous vegeta-tion, usually flooded or lia… |
| TOP | [Trees sparse natural vegetation](classes/TOP.md) | Natural open trees, occasionally with sparse or closed her-baceous vegetation cover, with percent-age cover v… |
| TFP | [Tree forest plantations](classes/TFP.md) | Tree forest plantation refers to governmental plantation. This class can be identified with large area and re… |
| TCL | [Trees dense natural vegetation](classes/TCL.md) | Natural closed trees with tree percentage cover of more than 60%. In Punjab the forest cover is limited, and … |
| SDU | [Sand dunes](classes/SDU.md) | Bare area/undifferentiated area not used for cultivation and usually devoid of grass and shrub cover. Non-veg… |
| BSO | [Bare soil](classes/BSO.md) | Bare area/undifferentiated area not used for cultivation and usually devoid of grass and shrub cover. Non-veg… |
| BTW | [Bare soil in temporary wet](classes/BTW.md) | Part of the river bed flooded during the rainy season (flood plain). |
| WBO | [Water bodies](classes/WBO.md) | Natural and artificial non-perennial fresh water body (flowing and standing). |
| WET | [Wetlands](classes/WET.md) | Wetlands are herbaceous vege-tation with cover ranging from 60% to 100% found in flood-ed/wet areas, sometime… |
