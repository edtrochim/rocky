---
id: registry:L31:SWe
kind: class
title: SWe Seasonal wetland
system: registry:L31
code: SWe
name: Seasonal wetland
status: registered
decomposed: true
file_class_id: 9A
n_rows: 33
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L31
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L31/L31.lccs
schema: okf/0.1
---

# SWe Seasonal wetland

## Definition (verbatim, FAO LCLR)

Seasonal wetlands resultant from summer rains (September to May), and typically occur in low areas in woods and open fields. Water is present during the rain season and exceed for a month.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 9B | 9C Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_period 3.0–6.0 |  |
| 9B | A0 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 10.0–30.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `9A`.
