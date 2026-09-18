---
id: registry:L28:Bsc
kind: class
title: Bsc Bushland scattered cultivation
system: registry:L28
code: Bsc
name: Bushland scattered cultivation
status: registered
decomposed: true
file_class_id: '46'
n_rows: 31
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L28
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L28/L28.lccs
schema: okf/0.1
---

# Bsc Bushland scattered cultivation

## Definition (verbatim, FAO LCLR)

Includes shifting cultivation. Shrub height between 1-3 m with combined cover of rainfed herbaceous crop area.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 47 | 48 Mandatory | `LC_Shrub` | Mandatory |  | height 1.0–3.0 | LC_VegetationArtificialityCharacteristic |
| 47 | 4B Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_CultivatedAndManagedVegetationCharacteristics (elements/LC_Characteristic[LC_Rainfed]/name=Rainfed, elements/LC_Characteristic[LC_Rainfed]/description=Describe the rainfed) |

Full rows: `../elements.csv`, class_id `46`.
