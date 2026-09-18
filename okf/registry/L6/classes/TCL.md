---
id: registry:L6:TCL
kind: class
title: TCL Trees dense natural vegetation
system: registry:L6
code: TCL
name: Trees dense natural vegetation
status: registered
decomposed: true
file_class_id: '15'
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_Tree
links:
- rel: in_system
  id: registry:L6
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L6/L6.lccs
schema: okf/0.1
---

# TCL Trees dense natural vegetation

## Definition (verbatim, FAO LCLR)

Natural closed trees with tree percentage cover of more than 60%. Forest cover is limited, and it is predominantly scrub forest. The conif-erous forests are mainly present in the northern mountainous areas.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 16 | 17 Mandatory | `LC_Tree` | Mandatory | 60.0–100.0 | LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/description=Contains the elements of Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/name=Woody Growth Leaf Phenology; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/description=Describe an Evergreen leaf phenology element; LC_WoodyGrowthLeafPhenology[LC_WoodyGrowthLeafPhenology]/elements/LC_WoodyLeafPhenology[LC_Evergreen]/name=Evergreen | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `15`.
