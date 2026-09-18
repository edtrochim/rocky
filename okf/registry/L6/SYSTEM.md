---
id: registry:L6
kind: system
title: Land cover legend for the land cover map of Sindh, Khyber Pakhtunkhwa and Balochistan provinces
alpha_code: L6
country: Pakistan
m49: 586
iso3: PAK
year: 2021
status: valid
legend_type: LCCS3
format: lccs3
publisher: Food and Agriculture Organization of the United Nations
reference_link: '-'
reference_file: Ref_6.pdf
n_classes_index: 17
n_classes_file: 17
n_classes_matched: 17
n_datasets: 3
files:
- okf/registry/_raw/L6/L6.csv
- okf/registry/_raw/L6/L6.eapx
- okf/registry/_raw/L6/L6.lccs
- okf/registry/_raw/L6/L6.xsd
vocabulary:
  errors: 1
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L6:BSO
  path: classes/BSO.md
- rel: has_class
  id: registry:L6:BTW
  path: classes/BTW.md
- rel: has_class
  id: registry:L6:BUP
  path: classes/BUP.md
- rel: has_class
  id: registry:L6:HCF
  path: classes/HCF.md
- rel: has_class
  id: registry:L6:HCI
  path: classes/HCI.md
- rel: has_class
  id: registry:L6:HCR
  path: classes/HCR.md
- rel: has_class
  id: registry:L6:HER
  path: classes/HER.md
- rel: has_class
  id: registry:L6:ORC
  path: classes/ORC.md
- rel: has_class
  id: registry:L6:SCL
  path: classes/SCL.md
- rel: has_class
  id: registry:L6:SDU
  path: classes/SDU.md
- rel: has_class
  id: registry:L6:SOP
  path: classes/SOP.md
- rel: has_class
  id: registry:L6:SWE
  path: classes/SWE.md
- rel: has_class
  id: registry:L6:TCL
  path: classes/TCL.md
- rel: has_class
  id: registry:L6:TOP
  path: classes/TOP.md
- rel: has_class
  id: registry:L6:WBO
  path: classes/WBO.md
- rel: has_class
  id: registry:L6:WET
  path: classes/WET.md
- rel: has_class
  id: registry:L6:SNW
  path: classes/SNW.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# Land cover legend for the land cover map of Sindh, Khyber Pakhtunkhwa and Balochistan provinces

Pakistan · 2021 · LCCS3 · status valid. Publisher: Food and Agriculture Organization of the United Nations. 17 classes in the registry index, 17 in the legend file, 17 matched by code or name.

Reference: Land cover mapping for Sindh, Khyber Pakhtunkhwa and Balochistan provinces (2021), -

## Datasets (3)

- Land cover map for Sindh province (iso/294a5318-97de-49d1-86a0-d04ac8ce48c5)
- Land cover map for Khyber Pakhtunkhwa province (iso/cb118283-1516-4c9b-920a-5411d0e6a6c0)
- Land cover map for Balochistan province (iso/9469451a-cb02-4b9d-91b9-b8de69b325f3)

## Vocabulary check of the registry file

1 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| BSO | [Bare soil](classes/BSO.md) | Bare area/undifferentiated area not used for cultivation and usually devoid of grass and shrub cover. Non-veg… |
| BTW | [Bare soil in temporary wet](classes/BTW.md) | Part of the river bed flooded during the rainy season (flood plain). |
| BUP | [Built-up](classes/BUP.md) | The land covered by build-ings, roads and artificial sur-faced areas. Different types of build-up are include… |
| HCF | [Herbaceous crops in flood plain](classes/HCF.md) | Herbaceous crop located only in proximity of the riverbed is termed as crop in floodplain. The water supply i… |
| HCI | [Herbaceous crops irrigated](classes/HCI.md) | Agricultural areas characterized by ex-tensive irrigational facilities. The pres-ence channels for irrigation… |
| HCR | [Herbaceous crops rainfed](classes/HCR.md) | Rainfed agricul-ture relies only on rainfall for water, therefore NDVI values strictly de-pend on rainfall pa… |
| HER | [Herbaceous natural vegetation](classes/HER.md) | Relatively dense herba-ceous natural vegeta-tion, occasionally with sparse shrubs and trees. NDVI values are … |
| ORC | [Tree orchards](classes/ORC.md) | Orchards are areas cultivated for the production of fruits, nuts, and other type of plan-tations. Areas cov-e… |
| SCL | [Shrubs dense natural vegetation](classes/SCL.md) | Natural closed shrubs with shrubs percent-age cover of more than 60%. |
| SDU | [Sand dunes](classes/SDU.md) | Bare area/undifferenti-ated area not used for cultivation and usually devoid of grass and shrub cover. Non-ve… |
| SOP | [Shrubs sparse natural vegetation](classes/SOP.md) | Natural open shrubs, occasionally with sparse or closed herbaceous vegetation cover, with percentage cover va… |
| SWE | [Shrubs in temporary wet soil](classes/SWE.md) | This class includes areas mainly covered by shrubs often with herbaceous vegetation, usually flooded or liabl… |
| TCL | [Trees dense natural vegetation](classes/TCL.md) | Natural closed trees with tree percentage cover of more than 60%. Forest cover is limited, and it is predomin… |
| TOP | [Trees sparse natural vegetation](classes/TOP.md) | Natural open trees, occasionally with sparse or closed herbaceous vege-tation cover, with percentage cover va… |
| WBO | [Water bodies](classes/WBO.md) | Natural and artificial non-perennial fresh water body (flowing and stand-ing). |
| WET | [Wetland](classes/WET.md) | Wetlands are herbaceous vegetation with cover rang-ing from 60% to 100% found in flooded/wet areas, some-time… |
| SNW | [Snow](classes/SNW.md) | This class includes snow permanent, glaciers and glacier with debris. Snow permanent is the area characterize… |
