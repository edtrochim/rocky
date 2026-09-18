---
id: registry:L31:DMF
kind: class
title: DMF Dense Miombo forest
system: registry:L31
code: DMF
name: Dense Miombo forest
status: registered
decomposed: true
file_class_id: 6C
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

# DMF Dense Miombo forest

## Definition (verbatim, FAO LCLR)

The miombo woodland or “panda forest” is a type of vegetation where trees, belonging to the genera Brachystegia, Isoberlinia and Julbernardia, predominate. Dense miombo is considered when there is a high concentration of trees (canopy cover above 50%). The land cover area in a zone can be between 80 to 100%

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 6D | 6E Mandatory | `LC_WoodyGrowthForm` | Mandatory | 40.0–100.0 | height 4.0–8.0; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/description=Describe an Evergreen leaf phenology element; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/name=Evergreen; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/percentage 90.0–100.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `6C`.
