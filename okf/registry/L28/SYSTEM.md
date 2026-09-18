---
id: registry:L28
kind: system
title: National land cover legend for Tanzania
alpha_code: L28
country: United Republic of Tanzania
m49: 834
iso3: TZA
year: 2020
status: valid
legend_type: LCCS3
format: lccs3
publisher: Tanzania Forest Service Agency
reference_link: ''
reference_file: Ref_28.pdf
n_classes_index: 25
n_classes_file: 27
n_classes_matched: 25
n_datasets: 1
files:
- okf/registry/_raw/L28/L28.csv
- okf/registry/_raw/L28/L28.eapx
- okf/registry/_raw/L28/L28.lccs
- okf/registry/_raw/L28/L28.xsd
vocabulary:
  errors: 0
  warnings: 0
links:
- rel: in_registry
  id: registry
  path: ../INDEX.md
- rel: has_class
  id: registry:L28:Bd
  path: classes/Bd.md
- rel: has_class
  id: registry:L28:Bo
  path: classes/Bo.md
- rel: has_class
  id: registry:L28:Bsc
  path: classes/Bsc.md
- rel: has_class
  id: registry:L28:Bsl
  path: classes/Bsl.md
- rel: has_class
  id: registry:L28:Bt
  path: classes/Bt.md
- rel: has_class
  id: registry:L28:Cbc
  path: classes/Cbc.md
- rel: has_class
  id: registry:L28:Cgc
  path: classes/Cgc.md
- rel: has_class
  id: registry:L28:Cwc
  path: classes/Cwc.md
- rel: has_class
  id: registry:L28:Fhm
  path: classes/Fhm.md
- rel: has_class
  id: registry:L28:FL
  path: classes/FL.md
- rel: has_class
  id: registry:L28:Fm
  path: classes/Fm.md
- rel: has_class
  id: registry:L28:Fp
  path: classes/Fp.md
- rel: has_class
  id: registry:L28:Gb
  path: classes/Gb.md
- rel: has_class
  id: registry:L28:Go
  path: classes/Go.md
- rel: has_class
  id: registry:L28:Gsc
  path: classes/Gsc.md
- rel: has_class
  id: registry:L28:Gw
  path: classes/Gw.md
- rel: has_class
  id: registry:L28:Ice
  path: classes/Ice.md
- rel: has_class
  id: registry:L28:ICaf
  path: classes/ICaf.md
- rel: has_class
  id: registry:L28:IWo
  path: classes/IWo.md
- rel: has_class
  id: registry:L28:Other
  path: classes/Other.md
- rel: has_class
  id: registry:L28:Ro
  path: classes/Ro.md
- rel: has_class
  id: registry:L28:Sc
  path: classes/Sc.md
- rel: has_class
  id: registry:L28:Wi
  path: classes/Wi.md
- rel: has_class
  id: registry:L28:Wo
  path: classes/Wo.md
- rel: has_class
  id: registry:L28:WsC
  path: classes/WsC.md
sources:
- https://us-central1-fao-maps-review.cloudfunctions.net/getLandCoverLegend
schema: okf/0.1
---

# National land cover legend for Tanzania

United Republic of Tanzania · 2020 · LCCS3 · status valid. Publisher: Tanzania Forest Service Agency. 25 classes in the registry index, 27 in the legend file, 25 matched by code or name.

Reference: National Forest Resources Monitoring and Assessment of Tanzania Mainland (2015), 

## Datasets (1)

- Land cover and land use for Tanzania (iso/61917c9a-715d-41c6-8c3e-df0a22904f01)

## Vocabulary check of the registry file

0 errors, 0 warnings from `rocky.validate` (see `elements.csv`).

## Classes

| code | class | definition |
|---|---|---|
| Bd | [Bushland dense](classes/Bd.md) | Land not defined as "forest", spanning more than 0.5 ha with shrub height between 1-3 m and a cover of 40-100… |
| Bo | [Bushland open](classes/Bo.md) | Land not defined as "forest", shrubs height between 1-3 m sometimes combined with trees. It does not include … |
| Bsc | [Bushland scattered cultivation](classes/Bsc.md) | Includes shifting cultivation. Shrub height between 1-3 m with combined cover of rainfed herbaceous crop area. |
| Bsl | [Open land bare soil](classes/Bsl.md) | Natural bare surface around larger lakes and disturbed areas. |
| Bt | [Bushland thicket](classes/Bt.md) | Land not defined as “Forest”, trees lower than 5 m and a canopy cover of 0.1-15%, or trees able to reach thes… |
| Cbc | [Cultivated land herbaceous crops](classes/Cbc.md) | Various herbaceous crops e.g. Cotton, vegetables, sisal, tobacco, flower plantations etc. |
| Cgc | [Cultivated land grain crops](classes/Cgc.md) | Various types of grass crops e.g., maize, wheat, millet, rice, sorghum. |
| Cwc | [Cultivated land wooded crops](classes/Cwc.md) | Monocultures and mixed crops of Tea, Cashew nuts, Cloves, mangoes, oranges etc. |
| Fhm | [Forest humid montane](classes/Fhm.md) | Land spanning more than 0.5 ha with trees that have heights of between 20-50m with combined cover of natural … |
| FL | [Forest lowland](classes/FL.md) | Woody growth form with the geographical aspect of groundwater forests and some coastal forests, < 800 m asl. |
| Fm | [Forest mangrove](classes/Fm.md) | Area of forest and other wooded land with mangrove vegetation along coastal areas |
| Fp | [Forest plantation](classes/Fp.md) | Cultivation of trees. |
| Gb | [Grassland bushed](classes/Gb.md) | Natural herbaceous area with combined cover of shrubs. |
| Go | [Grassland open](classes/Go.md) | Natural herbaceous area with cover of 10-100% and used for hunting, recreation and grazing. |
| Gsc | [Grassland scattered cropland](classes/Gsc.md) | Cultivated rainfed herbaceous crops with natural herbaceous cover. |
| Gw | [Grassland wooded](classes/Gw.md) | Natural herbaceous cover area with some tree cover of less than 30 %. |
| Ice | [Open land ice cap / snow](classes/Ice.md) | Area cover with snow/ice cap. |
| ICaf | [Cultivated land agro-forestry system](classes/ICaf.md) | Home gardens with multi-storey tree covers shading other crops e.g. Banana, Coffee, beans and yams. |
| IWo | [Woodland closed](classes/IWo.md) | Beekeeping, Hunting, Recreation, Grazing, Conservation, Timber production |
| Other | [Other areas](classes/Other.md) | Urban and rural built-up areas, air fields, infrastructure (power lines, railways, mining sites etc). |
| Ro | [Open land rock outcrops](classes/Ro.md) | Places dominated by rocks |
| Sc | [Open land coastal bare land](classes/Sc.md) | Bare area along coastal side e.g. beach. |
| Wi | [Inland water](classes/Wi.md) | Inland water bodies generally include major rivers, lakes and water reservoirs. |
| Wo | [Water ocean](classes/Wo.md) | Water bodies include oceans. |
| WsC | [Water wetlands](classes/WsC.md) | Water-logged that are seasonally inundated. |
