---
id: registry:L15:SEEA-5
kind: class
title: SEEA 5 Grassland
system: registry:L15
code: SEEA 5
name: Grassland
status: registered
decomposed: true
file_class_id: '20'
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L15
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L15/L15.lccs
schema: okf/0.1
---

# SEEA 5 Grassland

## Definition (verbatim, FAO LCLR)

The category is composed of a main layer of natural herbaceous vegetation with a cover from 10 to 100 per cent.

## Description

This class includes any geographical area dominated by natural herbaceous plants (grasslands, prairies, steppes and savannahs) with a cover of 10 per cent or more, irrespective of different human and/or animal activities, such as grazing or selective fire management. Woody plants (trees and/or shrubs) can be present, assuming their cover is less that 10 per cent.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 21 | 22 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 10.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 21 | 25 Optional | `LC_WoodyGrowthForm` | Mandatory | 1.0–10.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `20`.
