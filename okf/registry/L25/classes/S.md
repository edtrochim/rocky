---
id: registry:L25:S
kind: class
title: S Savanna
system: registry:L25
code: S
name: Savanna
status: registered
decomposed: true
file_class_id: BE
n_rows: 31
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# S Savanna

## Definition (verbatim, FAO LCLR)

This class is very basic, and generic being constituted by one mandatory strata that defines the overall class aspect. The strata are constituted by one basic element herb with the cover percentage of 40-100% and height ranges from 80 - 300 cm.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| BF | C0 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 40.0–100.0 | height 80.0–300.0 | LC_VegetationArtificialityCharacteristic |
| BF | C3 Optional | `LC_WoodyGrowthForm` | Mandatory | 2.0–15.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `BE`.
