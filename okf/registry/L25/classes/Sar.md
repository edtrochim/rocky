---
id: registry:L25:Sar
kind: class
title: Sar Shrub savanna
system: registry:L25
code: Sar
name: Shrub savanna
status: registered
decomposed: true
file_class_id: DE
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Sar Shrub savanna

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of shrub savanna. It is constituted by one mandatory horizontal pattern that defines the overall class structure. The strata is constituted by one basic element herbaceous growth forms.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| DF | E0 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 40.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| DF | E3 Mandatory | `LC_Shrub` | Mandatory | 4.0–20.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `DE`.
