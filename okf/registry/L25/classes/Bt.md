---
id: registry:L25:Bt
kind: class
title: Bt Tiger bush
system: registry:L25
code: Bt
name: Tiger bush
status: registered
decomposed: true
file_class_id: A9
n_rows: 47
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
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

# Bt Tiger bush

## Definition (verbatim, FAO LCLR)

This class describes the generic aspect of a tiger bush. It is constituted by two mandatory horizontal pattern and one basic stratum that defines the overall class structure. In first horizontal pattern (cover: 40-70%) the strata are constituted by one basic element shrubs.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| AA | AB Mandatory | `LC_Shrub` | Mandatory | 50.0–100.0 | height 0.3–2.0 | LC_VegetationArtificialityCharacteristic |
| AA | AE Optional | `LC_HerbaceousGrowthForm` | Mandatory | 2.0–40.0 |  | LC_VegetationArtificialityCharacteristic |
| B1 | B2 Mandatory | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `A9`.
