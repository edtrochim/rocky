---
id: registry:L2:4SCOs
kind: class
title: 4SCOs Closed to open seasonally flooded shrubs
system: registry:L2
code: 4SCOs
name: Closed to open seasonally flooded shrubs
status: registered
decomposed: true
file_class_id: C2
n_rows: 50
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
- LC_WaterBody
links:
- rel: in_system
  id: registry:L2
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L2/L2.lccs
schema: okf/0.1
---

# 4SCOs Closed to open seasonally flooded shrubs

## Definition (verbatim, FAO LCLR)

Closed to open (15-100%) shrubs in temporarily flooded land (2-4 months)

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| C3 | 115 Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_period 2.0–4.0 | LC_ArtificialityCharacteristic (type=Natural) |
| C3 | C4 Mandatory | `LC_Shrub` | Mandatory | 15.0–100.0 | height 0.3–5.0 | LC_VegetationArtificialityCharacteristic |
| C3 | C9 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 10.0–100.0 | height 3.0–30.0 | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `C2`.
