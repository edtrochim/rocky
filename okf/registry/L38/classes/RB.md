---
id: registry:L38:RB
kind: class
title: RB River bank
system: registry:L38
code: RB
name: River bank
status: registered
decomposed: true
file_class_id: '70'
n_rows: 41
rows_in: ../elements.csv
element_refs:
- LC_GrowthForm
- LC_SoilSandDepositsSurfaceElement
- LC_WaterBody
links:
- rel: in_system
  id: registry:L38
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_GrowthForm
  path: ../../../vocab/elements/LC_GrowthForm.md
- rel: uses_type
  id: element:LC_SoilSandDepositsSurfaceElement
  path: ../../../vocab/elements/LC_SoilSandDepositsSurfaceElement.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L38/L38.lccs
schema: okf/0.1
---

# RB River bank

## Definition (verbatim, FAO LCLR)

River bank (soil/sand deposits) + perennial/periodic flowing fresh water

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 71 | 72 Mandatory | `LC_SoilSandDepositsSurfaceElement` | Mandatory |  |  |  |
| 71 | 74 Optional | `LC_GrowthForm` | Mandatory | 0.0–20.0 |  | LC_VegetationArtificialityCharacteristic |
| 71 | 76 Optional | `LC_WaterBody` | Mandatory |  | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months; dynamics=Flowing |  |

Full rows: `../elements.csv`, class_id `70`.
