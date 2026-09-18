---
id: registry:L21:Hc
kind: class
title: Hc Cropland
system: registry:L21
code: Hc
name: Cropland
status: registered
decomposed: true
file_class_id: 4D
n_rows: 28
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L21
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L21/L21.lccs
schema: okf/0.1
---

# Hc Cropland

## Definition (verbatim, FAO LCLR)

This category includes arable and tillage land, and agro-forestry systems where vegetation falls below the thresholds used for the forest land category.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 4E | 52 Optional | `LC_WoodyGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |
| 4E | 4F Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics |

Full rows: `../elements.csv`, class_id `4D`.
