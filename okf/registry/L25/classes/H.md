---
id: registry:L25:H
kind: class
title: H Herbs dominated area
system: registry:L25
code: H
name: Herbs dominated area
status: registered
decomposed: true
file_class_id: B9
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# H Herbs dominated area

## Definition (verbatim, FAO LCLR)

This level corresponds to an area of natural vegetation with the mandatory presence of herbs. Herbaceous growth covers 20% - 100% of the landscape.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| BA | BB Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 20.0–100.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `B9`.
