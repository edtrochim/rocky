---
id: registry:L41:H
kind: class
title: H Herbs Dominated
system: registry:L41
code: H
name: Herbs Dominated
status: registered
decomposed: true
file_class_id: 3F
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L41
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L41/L41.lccs
schema: okf/0.1
---

# H Herbs Dominated

## Definition (verbatim, FAO LCLR)

Areas dominated by herbaceous plants (>20% cover), commonly found in meadows, pastures, or steppe ecosystems.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 40 | 41 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 20.0–100.0 | LC_HerbaceousGrowthLeafPhenology[LC_HerbaceousGrowthLeafPhenology]/name=Herbaceous Growth Leaf Phenology; LC_HerbaceousGrowthLeafPhenology[LC_HerbaceousGrowthLeafPhenology]/description=Contains the elements of Herbaceous Growth Leaf Phenology; LC_HerbaceousGrowthLeafPhenology[LC_HerbaceousGrowthLeafPhenology]/elements/LC_HerbaceousLeafPhenology[LC_Perennial]/name=Perennial; LC_HerbaceousGrowthLeafPhenology[LC_HerbaceousGrowthLeafPhenology]/elements/LC_HerbaceousLeafPhenology[LC_Perennial]/description=Describe a Perennial herbaceous growth form leaf phenology | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `3F`.
