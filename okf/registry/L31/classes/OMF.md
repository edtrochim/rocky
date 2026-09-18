---
id: registry:L31:OMF
kind: class
title: OMF Open Miombo forest
system: registry:L31
code: OMF
name: Open Miombo forest
status: registered
decomposed: true
file_class_id: '64'
n_rows: 27
rows_in: ../elements.csv
element_refs:
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L31
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L31/L31.lccs
schema: okf/0.1
---

# OMF Open Miombo forest

## Definition (verbatim, FAO LCLR)

The miombo forest or “panda forest” is a type of vegetation where trees, belonging to the genera Brachystegia, Isoberlinia and Julbernardia, predominate. It is open when there is an average concentration of trees, having a canopy cover between 10 and 50%. The land cover area in a zone can be between 20 to 80%.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 65 | 66 Mandatory | `LC_WoodyGrowthForm` | Mandatory | 10.0–40.0 | height 4.0–8.0; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/description=Describe an Evergreen leaf phenology element; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/name=Evergreen; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/percentage 90.0–100.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `64`.
