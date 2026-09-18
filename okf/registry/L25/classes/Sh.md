---
id: registry:L25:Sh
kind: class
title: Sh Grass savanna
system: registry:L25
code: Sh
name: Grass savanna
status: registered
decomposed: true
file_class_id: E6
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

# Sh Grass savanna

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of grass savanna. It is constituted by one mandatory stratum that defines the overall class structure. The strata is constituted by one basic element herbaceous growth forms

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| E7 | E8 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 40.0–100.0 | height 80.0–300.0 | LC_VegetationArtificialityCharacteristic |
| E7 | EB Optional | `LC_WoodyGrowthForm` | Mandatory | 1.0–4.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `E6`.
