---
id: registry:L38:HCW
kind: class
title: HCW Grassland on wetland
system: registry:L38
code: HCW
name: Grassland on wetland
status: registered
decomposed: true
file_class_id: '217'
n_rows: 35
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WaterBody
links:
- rel: in_system
  id: registry:L38
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L38/L38.lccs
schema: okf/0.1
---

# HCW Grassland on wetland

## Definition (verbatim, FAO LCLR)

Herbaceous dominated vegetation in an usually flooded (4-12 months) or liable to flooding area

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 218 | 219 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory | 1.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 218 | 21C Mandatory | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months | LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `217`.
