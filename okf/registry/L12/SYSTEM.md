---
id: registry:L12
kind: system
title: National land cover legend for Lesotho
alpha_code: L12
country: Lesotho
m49: 426
iso3: LSO
year: 2014
status: valid
legend_type: LCCS3
format: lccs3
publisher: Food and Agriculture Organization of the United Nations
reference_link: http://www.fao.org/geospatial/resources/detail/en/c/1024551/
reference_file: Ref_12.pdf
n_classes_index: 29
n_classes_file: 29
n_classes_matched: 29
n_datasets: 1
files:
- okf/registry/_raw/L12/L12.csv
- okf/registry/_raw/L12/L12.eapx
- okf/registry/_raw/L12/L12.lccs
- okf/registry/_raw/L12/L12.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L12:BA
  path: classes/BA.md
- rel: has_class
  id: registry:L12:BLR
  path: classes/BLR.md
- rel: has_class
  id: registry:L12:BR
  path: classes/BR.md
- rel: has_class
  id: registry:L12:GR
  path: classes/GR.md
- rel: has_class
  id: registry:L12:GRD
  path: classes/GRD.md
- rel: has_class
  id: registry:L12:GU
  path: classes/GU.md
- rel: has_class
  id: registry:L12:HCER
  path: classes/HCER.md
- rel: has_class
  id: registry:L12:HCIR
  path: classes/HCIR.md
- rel: has_class
  id: registry:L12:HCP
  path: classes/HCP.md
- rel: has_class
  id: registry:L12:HCSM
  path: classes/HCSM.md
- rel: has_class
  id: registry:L12:HCT
  path: classes/HCT.md
- rel: has_class
  id: registry:L12:MQ
  path: classes/MQ.md
- rel: has_class
  id: registry:L12:RB
  path: classes/RB.md
- rel: has_class
  id: registry:L12:RH1
  path: classes/RH1.md
- rel: has_class
  id: registry:L12:RH2
  path: classes/RH2.md
- rel: has_class
  id: registry:L12:SH1
  path: classes/SH1.md
- rel: has_class
  id: registry:L12:SH2
  path: classes/SH2.md
- rel: has_class
  id: registry:L12:TBL1
  path: classes/TBL1.md
- rel: has_class
  id: registry:L12:TBL2
  path: classes/TBL2.md
- rel: has_class
  id: registry:L12:TM1
  path: classes/TM1.md
- rel: has_class
  id: registry:L12:TM2
  path: classes/TM2.md
- rel: has_class
  id: registry:L12:TNL1
  path: classes/TNL1.md
- rel: has_class
  id: registry:L12:TNL2
  path: classes/TNL2.md
- rel: has_class
  id: registry:L12:TS
  path: classes/TS.md
- rel: has_class
  id: registry:L12:UA1
  path: classes/UA1.md
- rel: has_class
  id: registry:L12:UA2
  path: classes/UA2.md
- rel: has_class
  id: registry:L12:WB1
  path: classes/WB1.md
- rel: has_class
  id: registry:L12:WB2
  path: classes/WB2.md
- rel: has_class
  id: registry:L12:WET
  path: classes/WET.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# National land cover legend for Lesotho

Lesotho · 2014 · LCCS3 · status valid. Publisher: Food and Agriculture Organization of the United Nations. 29 classes in the registry index, 29 in the legend file, 29 matched by code or name.

Reference: Land Cover Atlas of Lesotho (2014), http://www.fao.org/geospatial/resources/detail/en/c/1024551/

## Datasets (1)

- Land cover of Lesotho (2014) (iso/c04cb8f9-aace-4abe-aa07-79e39312fbb2)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| BA | [Bare area](classes/BA.md) | Undifferentiated areas not used for cutivation and usually devoid of grass or shrub cover, commonly associate… |
| BLR | [Boulder and loose rock](classes/BLR.md) | Areas with large scattered boulders and/or unconsolidated loose rocks, commonly sloping and associated with r… |
| BR | [Bare rock](classes/BR.md) | Rock outcropsm commonly located at plateau edges. |
| GR | [Grassland](classes/GR.md) | Relatively dense natural vegetation, occasionally with sparse shrubs. |
| GRD | [Grassland - degraded](classes/GRD.md) | Degraded grassland with low vegetation cover, ocassionally bare with scattered rock outcrops; noticeably in s… |
| GU | [Gullies](classes/GU.md) | Gully erosion, commonly associated with river beds, occasionally with trees and/or tall shrubs. |
| HCER | [Rainfed agriculture, sheet erosion](classes/HCER.md) | Rainfed herbaceous crops with visible water sheet erosion, commonly with associated gully erosion. |
| HCIR | [Irrigated agriculture](classes/HCIR.md) | Small size irrigated herbaceous crops near water courses. |
| HCP | [Rainfed agriculture, plain areas](classes/HCP.md) | Rainfed herbaceous crops cultivated in flat-lying plains (slope up to 10 degrees) relatively larger sized fie… |
| HCSM | [Rainfed agriculture, sloping & mountaineous regions](classes/HCSM.md) | Rainfed herbaceous crops in sloping land and mountains (slope greater than 10 degrees) with terracing and/or … |
| HCT | [Rainfed agriculture + rainfed orchards](classes/HCT.md) | Small rainfed herbaceous crops + regular rainfed orchard plantation (usually as rows of fruit trees separatin… |
| MQ | [Mines & quarries](classes/MQ.md) | Major mines and quarries as well as temporary building material extraction and dumping sites. |
| RB | [River bank](classes/RB.md) | River bank (soil / sand deposits) + perenial or periodic flowing fresh water (river), occasionally with loose… |
| RH1 | [Rural settlements (plain area)](classes/RH1.md) | Rural houses in flat lying plain areas (slop up to 5 degrees) + small cultivated herbaceous crops + closed he… |
| RH2 | [Rural settlements (sloping and mountaneous area)](classes/RH2.md) | Rural houses in sloping and mountaneous areas (slope greater than 5 degrees) + herbaceous natural vegetation,… |
| SH1 | [Shrubland (closed)](classes/SH1.md) | Closed natural shrubs (H=0.5 to 1.5m), commonly observed on river valley slopes, ocassionally with scattered … |
| SH2 | [Shrubland (open)](classes/SH2.md) | Closed natural shrubs (H=0.5 to 1.5m), commonly observed on river valley slopes, ocassionally with scattered … |
| TBL1 | [Trees, broadleaved (closed)](classes/TBL1.md) | Closed deciduous broadleaved trees, commonly along river beds, sometimws observed as plantations. |
| TBL2 | [Trees, broadleaved (open)](classes/TBL2.md) | Open deciduous broadleaved trees + herbaceous natural vegetation. |
| TM1 | [Trees, undifferentiated (closed)](classes/TM1.md) | Closed undifferentiated trees, sometimes mixed broadleaved and needle-leaved; ocassionally with shrubs. |
| TM2 | [Trees, undifferentiated (open)](classes/TM2.md) | Closed undifferentiated trees + herbaceous natural vegetation. |
| TNL1 | [Trees, needle-leaved (closed)](classes/TNL1.md) | Closed evergreen needle-leaved trees, sometimes occuring as plantation. |
| TNL2 | [Trees, needle-leaved (open)](classes/TNL2.md) | Open evergreen needle-leaved trees + herbaceous natural vegetation. |
| TS | [Trees (sparse)](classes/TS.md) | Sparse scattered trees + herbaceous natural vegetation (closed to open). |
| UA1 | [Urban area](classes/UA1.md) | Relatively larger urban built-up areas, commonly with presence of trees, occasionally with small cultivated f… |
| UA2 | [Urban commercial and/or industrial](classes/UA2.md) | Commercial and/or industrial built-up areas, occasionally outside main urban and rural built-up areas. |
| WB1 | [Large waterbody](classes/WB1.md) | Large perennial fresh water lake or dam reservoir. |
| WB2 | [Small waterbody](classes/WB2.md) | Small fresh water seasonal and/or perennial reservoir, pool, etc. sometimes associated with nearly wetland ar… |
| WET | [Wetland (perennial and/or seasonal)](classes/WET.md) | Natural perennial and/or seasonal fresh waterbody + perennial closed-open natural vegetation. |
