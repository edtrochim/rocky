---
id: registry:L26
kind: system
title: Land cover legend for Somalia
alpha_code: L26
country: Somalia
m49: 706
iso3: SOM
year: 2015
status: valid
legend_type: LCCS3
format: lccs3
publisher: Food and Agriculture Organization of United Nations
reference_link: https://spatial.faoswalim.org/layers/geonode:SOM_Landcover_Owdweyne_Burao_FAOSWALIM#/a
reference_file: ''
n_classes_index: 19
n_classes_file: 19
n_classes_matched: 19
n_datasets: 1
files:
- okf/registry/_raw/L26/L26.csv
- okf/registry/_raw/L26/L26.eapx
- okf/registry/_raw/L26/L26.lccs
- okf/registry/_raw/L26/L26.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L26:BA
  path: classes/BA.md
- rel: has_class
  id: registry:L26:BU
  path: classes/BU.md
- rel: has_class
  id: registry:L26:GOC
  path: classes/GOC.md
- rel: has_class
  id: registry:L26:HCI
  path: classes/HCI.md
- rel: has_class
  id: registry:L26:HCR
  path: classes/HCR.md
- rel: has_class
  id: registry:L26:Man
  path: classes/Man.md
- rel: has_class
  id: registry:L26:SA
  path: classes/SA.md
- rel: has_class
  id: registry:L26:SC
  path: classes/SC.md
- rel: has_class
  id: registry:L26:SGS
  path: classes/SGS.md
- rel: has_class
  id: registry:L26:SO
  path: classes/SO.md
- rel: has_class
  id: registry:L26:SVO
  path: classes/SVO.md
- rel: has_class
  id: registry:L26:TC
  path: classes/TC.md
- rel: has_class
  id: registry:L26:TCI
  path: classes/TCI.md
- rel: has_class
  id: registry:L26:TO
  path: classes/TO.md
- rel: has_class
  id: registry:L26:TS
  path: classes/TS.md
- rel: has_class
  id: registry:L26:TVO
  path: classes/TVO.md
- rel: has_class
  id: registry:L26:WA
  path: classes/WA.md
- rel: has_class
  id: registry:L26:WB
  path: classes/WB.md
- rel: has_class
  id: registry:L26:WOC
  path: classes/WOC.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# Land cover legend for Somalia

Somalia · 2015 · LCCS3 · status valid. Publisher: Food and Agriculture Organization of United Nations. 19 classes in the registry index, 19 in the legend file, 19 matched by code or name.

Reference: Somalia Owdweyne & Burao Districts Land Cover FAOSWALIM (2015), https://spatial.faoswalim.org/layers/geonode:SOM_Landcover_Owdweyne_Burao_FAOSWALIM#/a

## Datasets (1)

- Somalia Owdweyne & Burao Districts Land Cover FAOSWALIM (-)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| BA | [Bare Area](classes/BA.md) | Optional layer of Growth forms (Herbs, Shrubs ans Trees) not exceeding 3% cover. |
| BU | [Builtup Areas](classes/BU.md) | Built-up surface. |
| GOC | [Grassland open to close](classes/GOC.md) | Natural Herbs with cover 21-80%. Optional Shrubs (0-15%). |
| HCI | [Herbaceous crop irrigated](classes/HCI.md) | Herbaceous crop irrigated (mainly spate irrigation). |
| HCR | [Herbaceous crop rainfed](classes/HCR.md) | Herbaceous crop rainfed |
| Man | [Mangroves](classes/Man.md) | Trees and shrubs mangroves. |
| SA | [Sand](classes/SA.md) | Loose and shifting sand. Optional layer of growth dorms (herbs, shrubs and trees) not exceeding 3% cover. |
| SC | [Shrubs close](classes/SC.md) | Natural shrubs with cover 66-100%. Optional trees (0-15%) and herbs (0-50%). |
| SGS | [Shrubs and grasses sparse](classes/SGS.md) | Natural herbs with cover (0-20%) with a layer of shrubs (0-15%). |
| SO | [Shrubs open](classes/SO.md) | Natural shrubs with cover 41-65%. Optional trees (0-15%) and herbs (0-50%). |
| SVO | [Shrubs very open](classes/SVO.md) | Natural shrubs with cover (16-40%). Optional trees (0-15%) and herbs (0-50%). |
| TC | [Trees close](classes/TC.md) | Natural trees with cover 66-100% with a layer of herbs (0-50%). Optional shrubs (0-15%). |
| TCI | [Tree crop irrigated](classes/TCI.md) | Tree crops, orchards and other tree plantation irrigated. |
| TO | [Trees open](classes/TO.md) | Natural trees with cover 41-65% with a layer of herbs (0-50%). Optional shrubs (0-15%). |
| TS | [Trees sparse](classes/TS.md) | Natural trees with cover 0-15% with a layer of herbs (0-50%). Optional shrubs (0-15%). |
| TVO | [Trees very open](classes/TVO.md) | Natural trees with cover 16-40% with a layer of herbs (0-50%). Optional shrubs (0-15%). |
| WA | [Wadi and riverbed](classes/WA.md) | Wadi and riverbed |
| WB | [Seasonal water bodies](classes/WB.md) | Seasonal water bodies. Bare soil when water is not present. |
| WOC | [Woodland open to close](classes/WOC.md) | Natural shrubs with cover 40-100% with a layer of trees (15-30%) and herbs (0-50%). |
