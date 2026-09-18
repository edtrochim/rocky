---
id: registry:L21:Hr
kind: class
title: Hr Paddy field
system: registry:L21
code: Hr
name: Paddy field
status: registered
decomposed: true
file_class_id: AA
n_rows: 41
rows_in: ../elements.csv
element_refs:
- LC_Graminoid
- LC_WaterBodyAndAssociatedSurfaceElement
links:
- rel: in_system
  id: registry:L21
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Graminoid
  path: ../../../vocab/elements/LC_Graminoid.md
- rel: uses_type
  id: element:LC_WaterBodyAndAssociatedSurfaceElement
  path: ../../../vocab/elements/LC_WaterBodyAndAssociatedSurfaceElement.md
sources:
- okf/registry/_raw/L21/L21.lccs
schema: okf/0.1
---

# Hr Paddy field

## Definition (verbatim, FAO LCLR)

Paddy field is a flooded parcel of arable land used for growing semiaquatic rice.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| AB | AC Mandatory | `LC_Graminoid` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_FieldSize]/name=Field Size, elements/LC_Characteristic[LC_FieldSize]/description=Describe the field size) |
| AB | B1 Optional | `LC_WaterBodyAndAssociatedSurfaceElement` | Mandatory | 80.0–100.0 | periodic_variation[LC_PeriodicVariations]/name=Periodic Variations; periodic_variation[LC_PeriodicVariations]/description=Contains the elements of Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/name=Periodic Variation; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/description=Describe a periodic variation element; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/period_type=Atmospheric; periodic_variation[LC_PeriodicVariations]/elements/LC_PeriodicVariation[LC_PeriodicVariation]/persistence_units=Months | LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `AA`.
