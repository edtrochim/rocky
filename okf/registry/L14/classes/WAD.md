---
id: registry:L14:WAD
kind: class
title: WAD Wady
system: registry:L14
code: WAD
name: Wady
status: registered
decomposed: true
file_class_id: BA
n_rows: 43
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L14
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L14/L14.lccs
schema: okf/0.1
---

# WAD Wady

## Definition (verbatim, FAO LCLR)

Bed of seasonal streams, usually dry, occasionally with very sparse woody vegetation (1-4%)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| BC | BD Mandatory | `LC_WoodyGrowthForm` | Mandatory | 1.0–4.0 |  | LC_VegetationArtificialityCharacteristic |
| BC | C0 Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Weeks; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_period 1.0–2.0 | LC_ArtificialityCharacteristic (type=Natural); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `BA`.
