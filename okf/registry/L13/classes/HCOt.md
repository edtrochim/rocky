---
id: registry:L13:HCOt
kind: class
title: HCOt Herbaceous Closed to Open Vegetation
system: registry:L13
code: HCOt
name: Herbaceous Closed to Open Vegetation
status: registered
decomposed: true
file_class_id: '27'
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L13
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L13/L13.lccs
schema: okf/0.1
---

# HCOt Herbaceous Closed to Open Vegetation

## Definition (verbatim, FAO LCLR)

It refers to natural herbaceous vegetation with a coverage percentage ranging from 15 to 100%.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 28 | 29 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 15.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `27`.
