---
id: registry:L2:2HCO-1H
kind: class
title: 2HCO//1H Closed to open herbaceous or Rainfed herbaceous crops
system: registry:L2
code: 2HCO//1H
name: Closed to open herbaceous or Rainfed herbaceous crops
status: registered
decomposed: true
file_class_id: '52'
n_rows: 27
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L2
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L2/L2.lccs
schema: okf/0.1
---

# 2HCO//1H Closed to open herbaceous or Rainfed herbaceous crops

## Definition (verbatim, FAO LCLR)

Closed to Open (15-100%) herbaceous vegetation or Rainfed herbaceous crop

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 53 | 54 Optional | `LC_HerbaceousGrowthForm` | Exclusive | 40.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 53 | 54 Optional | `LC_HerbaceousGrowthForm` | Exclusive |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed) |

Full rows: `../elements.csv`, class_id `52`.
