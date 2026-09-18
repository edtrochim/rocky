---
id: registry:L14
kind: system
title: National land cover legend for Jordan
alpha_code: L14
country: Jordan
m49: 400
iso3: JOR
year: 2017
status: valid
legend_type: LCCS3
format: lccs3
publisher: Food and Agriculture Organization of the United Nations
reference_link: http://www.fao.org/geospatial/resources/detail/en/c/1184337/
reference_file: Ref_14.pdf
n_classes_index: 34
n_classes_file: 35
n_classes_matched: 33
n_datasets: 1
files:
- okf/registry/_raw/L14/L14.csv
- okf/registry/_raw/L14/L14.eapx
- okf/registry/_raw/L14/L14.lccs
- okf/registry/_raw/L14/L14.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L14:IO
  path: classes/IO.md
- rel: has_class
  id: registry:L14:DP
  path: classes/DP.md
- rel: has_class
  id: registry:L14:HCI
  path: classes/HCI.md
- rel: has_class
  id: registry:L14:HCR
  path: classes/HCR.md
- rel: has_class
  id: registry:L14:TRC
  path: classes/TRC.md
- rel: has_class
  id: registry:L14:HCT
  path: classes/HCT.md
- rel: has_class
  id: registry:L14:TNL1
  path: classes/TNL1.md
- rel: has_class
  id: registry:L14:TM1
  path: classes/TM1.md
- rel: has_class
  id: registry:L14:TNL2
  path: classes/TNL2.md
- rel: has_class
  id: registry:L14:TM2
  path: classes/TM2.md
- rel: has_class
  id: registry:L14:OW
  path: classes/OW.md
- rel: has_class
  id: registry:L14:CW
  path: classes/CW.md
- rel: has_class
  id: registry:L14:GR
  path: classes/GR.md
- rel: has_class
  id: registry:L14:UA
  path: classes/UA.md
- rel: has_class
  id: registry:L14:IA
  path: classes/IA.md
- rel: has_class
  id: registry:L14:Uam
  path: classes/Uam.md
- rel: has_class
  id: registry:L14:SS
  path: classes/SS.md
- rel: has_class
  id: registry:L14:BS
  path: classes/BS.md
- rel: has_class
  id: registry:L14:SD
  path: classes/SD.md
- rel: has_class
  id: registry:L14:BR
  path: classes/BR.md
- rel: has_class
  id: registry:L14:BRG
  path: classes/BRG.md
- rel: has_class
  id: registry:L14:CH
  path: classes/CH.md
- rel: has_class
  id: registry:L14:BAS
  path: classes/BAS.md
- rel: has_class
  id: registry:L14:EX
  path: classes/EX.md
- rel: has_class
  id: registry:L14:WNS
  path: classes/WNS.md
- rel: has_class
  id: registry:L14:SA
  path: classes/SA.md
- rel: has_class
  id: registry:L14:WNF
  path: classes/WNF.md
- rel: has_class
  id: registry:L14:RB
  path: classes/RB.md
- rel: has_class
  id: registry:L14:WA
  path: classes/WA.md
- rel: has_class
  id: registry:L14:WP
  path: classes/WP.md
- rel: has_class
  id: registry:L14:WET
  path: classes/WET.md
- rel: has_class
  id: registry:L14:WAD
  path: classes/WAD.md
- rel: has_class
  id: registry:L14:MUDW
  path: classes/MUDW.md
- rel: has_class
  id: registry:L14:MUDD
  path: classes/MUDD.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# National land cover legend for Jordan

Jordan · 2017 · LCCS3 · status valid. Publisher: Food and Agriculture Organization of the United Nations. 34 classes in the registry index, 35 in the legend file, 33 matched by code or name.

Reference: Jordan land cover Atlas (2019), http://www.fao.org/geospatial/resources/detail/en/c/1184337/

## Datasets (1)

- Land cover of Jordan (2017) (iso/6dfcc76d-e0aa-439e-a10d-6366be3f23bc)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| IO | [Fruit tree orchards* including vineyards](classes/IO.md) | Fruit Tree orchards mainly near water course (Jordan valley) |
| DP | [Date palm plantation](classes/DP.md) | Regular date palm plantation |
| HCI | [Herbaceous crop irrigated](classes/HCI.md) | Irrigated Herbaceous crops mainly near water course (Jordan valley) and in the desert (water pumped from grou… |
| HCR | [Herbaceous crop rainfed](classes/HCR.md) | Rainfed cultivation of herbaceous crops |
| TRC | [Terraced rainfed crop](classes/TRC.md) | Terraced Rainfed crops in sloping land |
| HCT | [Herbaceous crop rainfed + orchard plantation](classes/HCT.md) | Rainfed cultivation of herbaceous crops + rainfed orchard plantation (olive) |
| TNL1 | [Closed needle-leaved trees](classes/TNL1.md) | Closed needle-leaved trees (40%-100%) |
| TM1 | [Closed trees (mixed leaf type)](classes/TM1.md) | Closed Trees Undifferentiated (40%-100%) |
| TNL2 | [Open needle-leaved trees](classes/TNL2.md) | Closed needle-leaved trees (10%-40%) |
| TM2 | [Open trees (mixed leaf type)](classes/TM2.md) | Open Trees Undifferentiated (10%-40%) |
| OW | [Sparse to very open woody vegetation](classes/OW.md) | Open woody vegetation (5-40 %) + Natural Herbaceous vegetation |
| CW | [Open to closed woody vegetation](classes/CW.md) | Closed woody vegetation (40-100 %) |
| GR | [Grassland sparse to very open](classes/GR.md) | Herbaceous Vegetation sparse to very open (5-40%) |
| UA | [Urban areas](classes/UA.md) | Urban build-up areas |
| IA | [Industrial and/or other areas](classes/IA.md) | Non urban built up areas and other construictions (industrial, airport, etc) |
| Uam | [Urban areas mixed with small cultivated fields and orchards](classes/Uam.md) | Urban build-up areas + small cultivated herbaceous crops + orchards and other plantation |
| SS | [Saline soil](classes/SS.md) | Expanse of ground covered with salt |
| BS | [Bare soil](classes/BS.md) | Bare areas -undifferentiated areas not used for cultivation and usually devoid of grass or shrub cover, commo… |
| SD | [Sandy areas](classes/SD.md) | Shifting and loosing sand not covered by vegetation and if present is negligible |
| BR | [Undifferentiated bare rock](classes/BR.md) | Rock outcrops |
| BRG | [Bare rock granite](classes/BRG.md) | Rock granite outcrops, commonly located in southern Jordan |
| CH | [Chert plain](classes/CH.md) | Flat expanse of ground covered with Chert stones and gravels commonly crossed by wady |
| BAS | [Basaltic plain](classes/BAS.md) | Flat expanse of ground covered with Basaltic stones and gravels |
| EX | [Extraction site](classes/EX.md) | Major mines and quarries as well as temporary building material extraction |
| WNS | [Waterbody natural saline](classes/WNS.md) | Saline water lake (Dead Sea) |
| SA | [Salt evaporation ponds](classes/SA.md) | Artificial ponds to extract salt from sea water |
| WNF | [Waterbody natural](classes/WNF.md) | Natural fresh water lake |
| RB | [River](classes/RB.md) | River Bank (bare soil) + Perennial or periodic flowing fresh water |
| WA | [Waterbody artificial](classes/WA.md) | Artificial fresh water lake (dam reservoir) |
| WP | [Water ponds](classes/WP.md) | Artificial fresh water, pool, ponds, small reservoirs |
| WET | [Seasonal wetland](classes/WET.md) | Seasonal fresh waterbody (2-8 weeks) + very open natural vegetation |
| WAD | [Wady](classes/WAD.md) | Bed of seasonal streams, usually dry, occasionally with very sparse woody vegetation (1-4%) |
| MUDW | [Wet mudflat](classes/MUDW.md) | Area regularly flooded. Flooding persists 4-8 months |
| MUDD | [Dry mudflat](classes/MUDD.md) | Mud deposits regularly flooded by stream. Flooding persists 1-2 months |
