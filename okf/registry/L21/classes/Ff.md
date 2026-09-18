---
id: registry:L21:Ff
kind: class
title: Ff Flooded forest
system: registry:L21
code: Ff
name: Flooded forest
status: registered
decomposed: true
file_class_id: 3A
n_rows: 51
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Tree
- LC_WaterBodyAndAssociatedSurfaceElement
links:
- rel: in_system
  id: registry:L21
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
- rel: uses_type
  id: element:LC_WaterBodyAndAssociatedSurfaceElement
  path: ../../../vocab/elements/LC_WaterBodyAndAssociatedSurfaceElement.md
sources:
- okf/registry/_raw/L21/L21.lccs
schema: okf/0.1
---

# Ff Flooded forest

## Definition (verbatim, FAO LCLR)

This forest type is found in Tonle Sap Lake. Most of the forests are low and disturbed. In many cases, there is only a mosaic remaining.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 3B | 42 Mandatory | `LC_HerbaceousGrowthForm` | Temporal Sequence Depending |  | sequential_temporal_relationship/type=Sequential Same Year; sequential_temporal_relationship/length 4.0–6.0 | LC_VegetationArtificialityCharacteristic |
| 3B | 42 Mandatory | `LC_WaterBodyAndAssociatedSurfaceElement` | Temporal Sequence Depending | 90.0–100.0 | sequential_temporal_relationship/type=Sequential Same Year; sequential_temporal_relationship/length 6.0–8.0; periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element | LC_WaterSalinityCharacteristic (type=Fresh) |
| 3B | 3C Mandatory | `LC_Tree` | Mandatory | 10.0–100.0 | height 3.0–16.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `3A`.
